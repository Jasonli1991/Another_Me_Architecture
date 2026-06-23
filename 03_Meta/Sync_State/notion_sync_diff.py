#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Notion 增量同步差異工具 (notion_sync_diff)
================================================
解決問題：每次都把整個公司的 Notion 匯出整批倒進 00_Raw/Inbox，
不想每次都全讀。靠「Notion 穩定 UUID + 內容 SHA-256」判斷差異，
下次只需讀「新增 + 變更」的檔案。

核心原理
--------
Notion 匯出的檔名帶一個 32 位 hex 的穩定 UUID（同一頁面不論匯出幾次、
內容怎麼改，UUID 不變）。內容雜湊(SHA-256)用來偵測內容是否變動。
  - UUID 沒見過            → 新頁面 (NEW，要讀)
  - UUID 見過 + hash 不同  → 內容更新 (CHANGED，要讀)
  - UUID 見過 + hash 相同  → 沒變 (UNCHANGED，跳過)
  - 上次有、這次沒有       → Notion 已刪 (DELETED，標記)
  - 無 UUID 的檔(內嵌圖等) → 用 hash 比對，重複就跳過

用法
----
# 1) 建立/更新 baseline 快照（同步完成後、清空 Inbox 前執行）
python3 notion_sync_diff.py snapshot \
    --inbox "../../00_Raw/Inbox" \
    --manifest "notion_manifest.json"

# 2) 下次有新匯出時，先比對差異（manifest = 上次的快照）
python3 notion_sync_diff.py diff \
    --inbox "../../00_Raw/Inbox" \
    --manifest "notion_manifest.json" \
    --report "last_diff.json"        # 可選：輸出差異報告 JSON

典型流程（下一次）
  diff  → 只讀 NEW+CHANGED → 處理 → snapshot(覆寫 manifest 更新狀態)
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

# Notion 檔名尾端的 32 位 hex id
UUID_RE = re.compile(r"([0-9a-f]{32})")

MEDIA_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mov"}


def sha256_of(path: str, buf: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(buf)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def title_from(basename: str) -> str:
    """去掉尾端 UUID 與副檔名，還原人類標題。"""
    stem, _ext = os.path.splitext(basename)
    m = UUID_RE.search(stem)
    if m:
        stem = stem[: m.start()].rstrip(" _-")
    return stem.strip()


def match_key(basename: str, uuid):
    """跨匯出穩定的邏輯身分鍵。
    Notion 資料庫會對同一 UUID 匯出多個檔（主視圖 .csv 與 _all.csv），
    故鍵需含 副檔名 + 是否 _all，避免同 UUID 碰撞誤判。
    無 UUID 的檔回傳 None（改用內容 hash 比對）。"""
    if not uuid:
        return None
    stem, ext = os.path.splitext(basename)
    all_flag = "all" if stem.endswith("_all") else "main"
    return f"{uuid}|{ext.lower()}|{all_flag}"


def scan(inbox: str) -> dict:
    """掃描 Inbox，回傳 {relpath: record}。"""
    entries = {}
    for root, _dirs, files in os.walk(inbox):
        for name in files:
            if name == ".gitkeep" or name.startswith("."):
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, inbox)
            ext = os.path.splitext(name)[1].lower()
            m = UUID_RE.search(name)
            try:
                size = os.path.getsize(full)
                digest = sha256_of(full)
            except OSError as e:
                print(f"  ! 讀取失敗 {rel}: {e}", file=sys.stderr)
                continue
            uuid = m.group(1) if m else None
            entries[rel] = {
                "path": rel,
                "basename": name,
                "title": title_from(name),
                "notion_uuid": uuid,
                "match_key": match_key(name, uuid),
                "ext": ext,
                "is_media": ext in MEDIA_EXT,
                "size": size,
                "sha256": digest,
                # 由同步流程回填：這份檔案被同步到哪（Dashboard/Wiki 路徑）
                "synced_to": None,
            }
    return entries


def load_manifest(path: str) -> dict:
    if not os.path.exists(path):
        return {"generated_at": None, "inbox": None, "files": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_snapshot(args) -> int:
    entries = scan(args.inbox)
    # 保留上一版已回填的 synced_to（依 match_key 或 sha 對應）
    prev = load_manifest(args.manifest).get("files", {})
    prev_by_key = {r["match_key"]: r for r in prev.values() if r.get("match_key")}
    prev_by_sha = {r["sha256"]: r for r in prev.values()}
    for rec in entries.values():
        old = None
        if rec["match_key"] and rec["match_key"] in prev_by_key:
            old = prev_by_key[rec["match_key"]]
        elif rec["sha256"] in prev_by_sha:
            old = prev_by_sha[rec["sha256"]]
        if old and old.get("synced_to"):
            rec["synced_to"] = old["synced_to"]

    manifest = {
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "inbox": os.path.abspath(args.inbox),
        "tool_version": "1.0",
        "count": len(entries),
        "files": entries,
    }
    with open(args.manifest, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    with_uuid = sum(1 for r in entries.values() if r["notion_uuid"])
    print(f"✅ snapshot 完成：{len(entries)} 檔 (帶 UUID {with_uuid} / 無 UUID {len(entries)-with_uuid})")
    print(f"   → {os.path.abspath(args.manifest)}")
    return 0


def cmd_diff(args) -> int:
    manifest = load_manifest(args.manifest)
    prev = manifest.get("files", {})
    if not prev:
        print("⚠️  manifest 不存在或為空 → 視為首次，全部都是 NEW（請改跑 snapshot）")
    prev_by_key = {r["match_key"]: r for r in prev.values() if r.get("match_key")}
    prev_by_sha = {r["sha256"]: r for r in prev.values()}

    cur = scan(args.inbox)
    new, changed, unchanged = [], [], []
    seen_prev_key, seen_prev_sha = set(), set()

    for rel, rec in sorted(cur.items()):
        key = rec["match_key"]
        if key and key in prev_by_key:
            old = prev_by_key[key]
            seen_prev_key.add(key)
            seen_prev_sha.add(old["sha256"])
            if old["sha256"] == rec["sha256"]:
                unchanged.append(rec)
            else:
                changed.append({**rec, "prev_title": old.get("title")})
        elif (not key) and rec["sha256"] in prev_by_sha:
            unchanged.append(rec)
            seen_prev_sha.add(rec["sha256"])
        else:
            new.append(rec)

    deleted = []
    for rel, old in prev.items():
        k = old.get("match_key")
        if k:
            if k not in seen_prev_key:
                deleted.append(old)
        else:
            if old["sha256"] not in seen_prev_sha:
                deleted.append(old)

    def names(lst):
        return [r["basename"] for r in lst]

    to_read = new + changed
    print("=" * 60)
    print(f"Notion 增量差異報告  (baseline: {manifest.get('generated_at') or '無'})")
    print("=" * 60)
    print(f"目前 Inbox 檔數 : {len(cur)}")
    print(f"🆕 NEW       新增  : {len(new)}")
    print(f"✏️  CHANGED   變更  : {len(changed)}")
    print(f"✅ UNCHANGED 不變  : {len(unchanged)}  (可跳過)")
    print(f"🗑️  DELETED   已刪  : {len(deleted)}")
    print("-" * 60)
    print(f"👉 本次只需讀 {len(to_read)} 檔（NEW+CHANGED），跳過 {len(unchanged)} 檔")
    print("-" * 60)
    if new:
        print("\n[NEW]")
        for n in names(new):
            print("  +", n)
    if changed:
        print("\n[CHANGED]")
        for n in names(changed):
            print("  ~", n)
    if deleted:
        print("\n[DELETED in Notion]")
        for n in names(deleted):
            print("  -", n)

    if args.report:
        report = {
            "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
            "baseline_at": manifest.get("generated_at"),
            "summary": {
                "current": len(cur), "new": len(new), "changed": len(changed),
                "unchanged": len(unchanged), "deleted": len(deleted),
                "to_read": len(to_read),
            },
            "new": [r["path"] for r in new],
            "changed": [r["path"] for r in changed],
            "unchanged": [r["path"] for r in unchanged],
            "deleted": [r["path"] for r in deleted],
            "read_paths_abs": [os.path.join(os.path.abspath(args.inbox), r["path"]) for r in to_read],
        }
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n📄 差異報告 → {os.path.abspath(args.report)}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Notion 增量同步差異工具")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("snapshot", help="建立/更新 baseline 快照")
    sp.add_argument("--inbox", required=True)
    sp.add_argument("--manifest", required=True)
    sp.set_defaults(func=cmd_snapshot)

    dp = sub.add_parser("diff", help="比對目前 Inbox 與上次快照的差異")
    dp.add_argument("--inbox", required=True)
    dp.add_argument("--manifest", required=True)
    dp.add_argument("--report", default=None, help="可選：輸出差異報告 JSON 路徑")
    dp.set_defaults(func=cmd_diff)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
