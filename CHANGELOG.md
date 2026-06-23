# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0] - 2026-06-23

### Added
- `LICENSE`: 採用 **MIT License**，授權範圍為知識庫框架（README、`03_Meta/` 的 Prompts／Templates／TAGS 及 `notion_sync_diff.py` 工具）。
- `README.md`: 新增「📜 授權 (License)」段落。
- Notion 同步 SOP 新增「增量同步（差異偵測）」小節，並新增 `03_Meta/Sync_State/notion_sync_diff.py`：以 Notion 穩定 UUID + 內容 SHA-256 偵測 NEW／CHANGED／DELETED，下次整批匯出只讀差異檔，免全庫重讀。

### Changed
- `README.md`: 更新頂部最新更新橫幅與頁尾至 v1.2.0。
- `.gitignore`: 忽略 `03_Meta/Sync_State/*.json`（含公司 Notion 頁面標題的同步狀態資料，不對外公開）。

## [1.1.0] - 2026-05-10

### Added
- `03_Meta/TAGS.md`: 新增標籤管理系統說明，定義知識庫標籤規範。

### Changed
- `03_Meta/Prompts/AI_Compiler_Prompt.md`: 優化 AI 編譯器提示詞，強化雙向連結與標籤引用邏輯。
- `03_Meta/Prompts/System_Auditor_Prompt.md`: 優化系統稽核提示詞，增加標籤審計功能。
- `03_Meta/Templates/Concept_Template.md`: 更新概念筆記模板，新增 YAML 欄位與結構優化。
- `03_Meta/Templates/Summary_Template.md`: 更新摘要筆記模板。
- `README.md`: 更新專案說明，新增最新更新區塊，並同步架構地圖。
