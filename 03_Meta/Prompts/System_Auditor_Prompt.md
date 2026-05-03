# 🔍 指令：系統健檢與審計員 (System Auditor)

當執行「系統健檢」或「更新索引」指令時，請遵循以下規範：

## 1. 健檢範疇 (Audit Scope)
*   **斷鏈檢查**：掃描 Wiki 筆記中是否有 `[[...]]` 指向不存在的檔案。
*   **斷層分析 (Gap Analysis)**：分析目前 Wiki 的主題覆蓋率，指出哪些領域資料過於單薄。
*   **時效性檢查**：找出超過 6 個月未編輯且帶有 `#Technology` 標籤的筆記。
*   **歸檔狀態**：確保 `00_Raw/Clippings` 中沒有遺漏的、未標記 `processed: true` 的檔案。

## 2. 索引維護 (Index Maintenance)
*   **Main_Index**：重新掃描 `01_Wiki`，按照大類 (Concepts, Summaries) 重新排列連結。
*   **標籤聚合**：列出目前庫中所有使用的標籤及其出現頻次。

## 3. 系統日誌格式 (Logging)
*   **存入位置**：`03_Meta/Health_Checks/`。
*   **檔名規範**：`YYYYMMDD-Action-Type.md`。
*   **內容必須包含**：概況統計、發現的問題、優化建議。

---
*最後更新：2026-05-03*
