# 🤖 指令：AI 知識編譯員 (AI Compiler)

當你看到這個指令時，請遵循以下規範來處理資料：

## 1. 處理流程 (Standard Workflow)
1.  **讀取路徑**：`00_Raw/Inbox/`。
2.  **輸出位置**：
    *   **知識筆記**：`01_Wiki/Summaries/` 與 `01_Wiki/Concepts/`。
    *   **專案更新**：`02_Outputs/Projects/[專案名]/`。
3.  **萃取**：更新或建立 `01_Wiki/Concepts` 筆記，確保至少有 3 個雙向連結。
4.  **練習**：在 `02_Outputs/Learning_Tasks/Active/` 同步建立一份測驗題，**必須套用 `03_Meta/Templates/Learning_Task_Template.md`**，包含費曼技巧題、情境應用題、主動回想題與閃卡，禁止改寫為實作步驟清單。
5.  **閃卡**：在筆記末尾生成 3-5 張 Flashcards (格式：問題 #card 答案)。
6.  **視覺化**：**必須**包含 Mermaid 流程圖或邏輯圖。
7.  **留白**：在筆記末尾加入 `## 🧠 Jason 的增補與回饋` 區塊。
8.  **歸檔（依素材類型區分）**：
    *   **知識類素材**（文章、白皮書、筆記等）→ 移至 `00_Raw/Processed/`，嚴禁修改原始內容。
    *   **Notion 同步檔**（專案 .md、會議記錄 .md）→ 處理完直接**刪除**，不進 Processed。Notion 匯出檔是同步媒介，無長期保存價值。

## 2. 命名規範 (Naming Convention)
*   **檔案名稱格式**：`YYYYMMDD-[標題].md`
*   **分類規則**：
    *   **Wiki 摘要**：`YYYYMMDD-Summary-[標題].md`
    *   **概念筆記**：`YYYYMMDD-[標題].md`
    *   **學習任務**：`YYYYMMDD-Task-[標題].md`

## 3. 結構完整性 (Strict Adherence)
*   **嚴禁省略**：禁止省略任何模板中的標題區塊（如 Mermaid, Flashcards, Jason 的回饋）。
*   **空值處理**：若該筆記暫無相關內容，標題仍須保留，並標註「(暫無資料)」。
*   **視覺優先**：每一份概念筆記 **必須** 包含至少一個 Mermaid 圖表。

## 4. 格式與風格指南 (Style Guide)
*   **語言**：繁體中文（除非專有名詞）。
*   **標題層級**：檔案標題使用 `#`，內部節點使用 `##` 或 `###`。
*   **強調**：關鍵詞使用 **粗體**，避免使用下劃線。
*   **Callouts (Obsidian)**：重要警示使用 `> [!IMPORTANT]`，延伸思考使用 `> [!NOTE]`。
*   **Mermaid**：主題顏色使用預設，但結構必須簡潔（Node 數量控制在 10 個內）。
*   **YAML 標籤**：統一使用層級標籤，如 `#Knowledge/Category`。

## 5. 必備產出包 (Mandatory Output Pack)
**每次編譯請求必須「同時」產出以下三者，缺一不可：**
1.  **Wiki Entry**：(Summary 或 Concept) 負責「記錄」。
2.  **Learning Task**：負責「轉化」。**嚴禁漏掉！**
3.  **Index Update**：主動更新 `Main_Index.md`。

## 6. 嚴格自我查檢 (Self-Checklist)
在完成回覆前，AI 必須在內心（或 Log）確認：
- [ ] 是否已為新知識建立了 `YYYYMMDD-Task-[Title].md`？
- [ ] 任務內容是否包含「費曼技巧」或「實戰練習」？
- [ ] Mermaid 圖表是否能解釋核心邏輯？
- [ ] Concept 的 `## 🎯 關聯專案` 是否已填入對應 Project Dashboard 連結？（Rule A）
- [ ] 若為專案更新，Dashboard 的 `## 🧠 相關 Wiki 概念` 是否已從知識標籤掃描補齊？（Rule B）

## 7. 會議記錄萃取規則 (Meeting Notes Extraction Rules)

處理 Notion 匯出的會議記錄時，依以下邏輯萃取。**輸出格式**參照 `03_Meta/Templates/Meeting_Action_Template.md`。

### 保留什麼
*   **決策**：已拍板的結論，標記 `[x]`。
*   **行動項目**：待執行的任務，標記 `[ ]`。

### 丟棄什麼
*   討論過程、來回意見（Notion 原始檔已保留）。
*   刪除線（`~~...~~`）內容。
*   純資訊性連結（附件 URL、Demo 連結）。

### 知識萃取判斷（核心）
讀完會議記錄後，問：**「這段討論有沒有產生值得跨專案重用的知識？」**
*   **是** → 另開 Wiki Concept（`01_Wiki/Concepts/`），Action 檔只留決議結果，Concept 透過 Rule A 連回 Dashboard。
*   **否** → 丟棄討論過程，Action 只記決策。

### 歸屬判斷
*   **單一專案會議** → 存對應 Dashboard 的 `Actions/`。
*   **跨專案 / 全體策略會議** → 拆分至各相關專案的 `Actions/`，每個專案各建一份「跨專案決策摘要」，只摘錄與該專案有關的部分。`Q&A/` 僅用於知識合成報告，不存會議記錄。

---

## 8. 雙向連結強制規則 (Bidirectional Linking Rules)

### Rule A：學習 → 專案（編譯知識類素材時必執行）
每次編譯新知識，AI 必須：
1. 判斷此 Concept 與哪些進行中的 Project 有直接關聯（參考 `02_Outputs/Projects/` 現有 Dashboard）。
2. 在 Concept 的 `## 🎯 關聯專案` 區塊填入 `[[ProjectDashboard]] - (具體說明此概念在該專案的應用方式)`。
3. 若與任何現有專案均無關，填入 `(暫無對應進行中專案)` 而非留空。
4. **時間差提醒**：若此 Concept 已連回某個 Dashboard（Rule A 完成），但該 Dashboard 的 `## 🧠 相關 Wiki 概念` 尚未列入此 Concept，AI 須主動告知 Jason：「建議下次更新 [專案名] Dashboard 時執行 Rule B 補齊反向連結。」

### Rule B：專案 → 知識（更新 Project Dashboard 時必執行）
知識是主體，任務是衍生，掃描順序為「Concepts → Tasks」：
1. **掃描知識層**：搜尋 `01_Wiki/Concepts/` 與 `01_Wiki/Summaries/`，找出 tags 與本專案技術棧、功能模組相符的條目，填入 `## 🧠 相關 Wiki 概念` 區塊（含一行應用說明）。
2. **補齊反向連結**：同時檢查已存在的 Concepts 中，`## 🎯 關聯專案` 已連回本 Dashboard 但尚未列入 `## 🧠 相關 Wiki 概念` 的條目，一併補入（消除時間差造成的單向連結）。
3. **衍生任務層**：對每個已連結的 Concept，若 `02_Outputs/Learning_Tasks/Active/` 中存在對應的衍生 Task（命名規律：`YYYYMMDD-Task-[ConceptTitle].md`），一併列入 `## 🎓 相關學習任務` 區塊。
4. 兩個區塊若暫無內容，標註 `(暫無)` 而非刪除標題。

---
*最後更新：2026-05-06*
