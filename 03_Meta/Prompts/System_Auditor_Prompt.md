# 🔍 指令：系統健檢與審計員 (System Auditor)

當執行「系統健檢」或「更新索引」指令時，請遵循以下規範：

## 1. 健檢範疇 (Audit Scope)

### 1-1 斷鏈檢查
*   掃描 `01_Wiki/` 所有筆記中的 `[[...]]` 連結，確認目標檔案存在。
*   掃描 `02_Outputs/Projects/` 所有 Dashboard 的 Actions 連結是否指向有效檔案。

### 1-2 雙向連結完整性（Rule A/B 審計）
*   **Rule A 缺口**：找出 `01_Wiki/Concepts/` 中 `## 🎯 關聯專案` 為空或填 `(暫無對應進行中專案)` 的條目，確認是否有新增專案可以補連結。
*   **Rule B 缺口**：找出已在 Concept 透過 Rule A 連回某 Dashboard，但該 Dashboard 的 `## 🧠 相關 Wiki 概念` 尚未列入的條目（單向連結），列出清單並提醒補齊。

### 1-3 斷層分析 (Gap Analysis)
*   分析目前 Wiki 的主題覆蓋率，指出哪些進行中專案的技術棧在 Concepts 中缺乏對應筆記。
*   找出 `02_Outputs/Projects/` 中的 Dashboard，其 `## 🧠 相關 Wiki 概念` 區塊標註 `(暫無)` 的專案，優先建議補齊。

### 1-4 時效性檢查
*   找出超過 6 個月未編輯且帶有 `#Technology` 標籤的 Wiki 筆記，標記為「可能過時」。

### 1-5 Inbox 清潔
*   確認 `00_Raw/Inbox/` 中沒有遺留未處理的素材。
*   確認 `00_Raw/Processed/` 中的知識類素材 YAML 都已加入 `processed: true`。
*   ⚠️ Notion 同步檔（專案 .md、會議記錄 .md）不應出現在 `Processed/`，若有則為錯誤歸檔。

### 1-6 Learning Task 狀態審查
*   掃描 `02_Outputs/Learning_Tasks/Active/` 中有 Jason 回答內容的任務，確認是否需要移至 `Completed/`。
*   確認所有任務格式符合 `03_Meta/Templates/Learning_Task_Template.md`（包含費曼技巧、實戰應用、閃卡三段）。

### 1-7 標籤一致性審查
*   **格式檢查**：掃描 `01_Wiki/Concepts/` 與 `01_Wiki/Summaries/`，檢查是否有違反命名規則的標籤：
    - ❌ 單數形式 `#Summary`（應為 `#Summaries`）
    - ❌ 層級符號 `#AI/Engineering` 或 `#Engineering/Workflow`（應為 `#AI-Engineering` 等）
    - ❌ 小寫標籤如 `#rag`, `#dify`（應為 CamelCase）
*   **過度標籤檢查**：找出超過 6 個標籤的檔案，評估是否需要簡化。
*   **孤立標籤檢查**：找出只出現 1 次的標籤，考慮是否應合併或移除。
*   **標籤雲更新**：掃描所有標籤，更新 `Main_Index.md` 的 `## 🏷️ 標籤雲` 區塊（僅納入出現 2 次以上的標籤）。

---

## 2. 索引維護 (Index Maintenance)

執行「更新索引」時，**必須依照 `03_Meta/Templates/Main_Index_Template.md` 的結構產出**，包含分區標題、分組順序、連結格式與狀態 emoji 規則。

*   重新掃描 `01_Wiki/Concepts/`，依分組規則（RAG 技術 → AI 基礎設施 → AI 工具平台 → 安全與合規 → 應用層 → PKM 系統）填入對應區塊。
*   重新掃描 `01_Wiki/Summaries/`，依日期由新到舊分組。
*   重新掃描 `02_Outputs/Projects/`，更新進行中專案表格（狀態從各 Dashboard YAML 讀取）。
*   重新掃描 `02_Outputs/Learning_Tasks/Active/`，更新學習任務清單。
*   **連結格式**：一律使用 vault 根路徑（如 `[[02_Outputs/Projects/...]]`），不使用相對路徑（`../../`）。
*   標籤聚合：掃描全庫 tags，取出現 2 次以上的標籤更新標籤雲。

---

## 3. 系統日誌格式 (Logging)

*   **存入位置**：`03_Meta/Health_Checks/`。
*   **檔名規範**：`YYYYMMDD-HealthCheck.md`。
*   **內容必須包含**：概況統計、發現的問題清單、優化建議、Rule A/B 缺口清單。

---
*最後更新：2026-05-10*
