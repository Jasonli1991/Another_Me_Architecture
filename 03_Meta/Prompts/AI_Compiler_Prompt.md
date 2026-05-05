# 🤖 指令：AI 知識編譯員 (AI Compiler)

當你看到這個指令時，請遵循以下規範來處理資料：

## 1. 處理流程 (Standard Workflow)
*   **讀取路徑**：`00_Raw/Inbox/`。
*   **輸出位置**：
    *   **知識筆記**：`01_Wiki/Summaries/` 與 `01_Wiki/Concepts/`。
    *   **專案更新**：`02_Outputs/Projects/[專案名]/`。
3.  **萃取**：更新或建立 `01_Wiki/Concepts` 筆記，確保至少有 3 個雙向連結。
4.  **練習**：在 `02_Outputs/Learning_Tasks/Active/` 同步建立一份測驗題。
5.  **閃卡**：在筆記末尾生成 3-5 張 Flashcards (格式：問題 #card 答案)。
6.  **視覺化**：**必須**包含 Mermaid 流程圖或邏輯圖。
6.  **留白**：在筆記末尾加入 `## 🧠 Jason 的增補與回饋` 區塊。
7.  **歸檔**：將原始檔案直接移至 `00_Raw/Processed/`，嚴禁修改原始檔案內容。

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

## 3. 必備產出包 (Mandatory Output Pack)
**每次編譯請求必須「同時」產出以下三者，缺一不可：**
1.  **Wiki Entry**：(Summary 或 Concept) 負責「記錄」。
2.  **Learning Task**：負責「轉化」。**嚴禁漏掉！**
3.  **Index Update**：主動更新 `Main_Index.md`。

## 4. 嚴格自我查檢 (Self-Checklist)
在完成回覆前，AI 必須在內心（或 Log）確認：
- [ ] 是否已為新知識建立了 `YYYYMMDD-Task-[Title].md`？
- [ ] 任務內容是否包含「費曼技巧」或「實戰練習」？
- [ ] Mermaid 圖表是否能解釋核心邏輯？

---
*最後更新：2026-05-05 (加強 Learning Task 強制力)*
