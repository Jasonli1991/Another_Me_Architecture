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
7.  **歸檔**：將原始檔案標註 `processed: true` 並移至 `00_Raw/Processed/`。

## 2. 格式與風格指南 (Style Guide)
*   **語言**：繁體中文（除非專有名詞）。
*   **標題層級**：檔案標題使用 `#`，內部節點使用 `##` 或 `###`。
*   **強調**：關鍵詞使用 **粗體**，避免使用下劃線。
*   **Callouts (Obsidian)**：重要警示使用 `> [!IMPORTANT]`，延伸思考使用 `> [!NOTE]`。
*   **Mermaid**：主題顏色使用預設，但結構必須簡潔（Node 數量控制在 10 個內）。
*   **YAML 標籤**：統一使用層級標籤，如 `#Knowledge/Category`。

## 3. 系統連動
*   處理完畢後，主動詢問用戶是否需要更新 `Main_Index` 或進行對話練習。

---
*最後更新：2026-05-03*
