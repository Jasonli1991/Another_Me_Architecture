# 🏷️ 標籤規範 (Tagging Convention)

本文檔定義 01_Wiki 中所有 Summaries 和 Concepts 檔案的標籤使用規範。

> **核心目的**：標籤用於支持 Rule A & Rule B 的自動掃描，確保知識與專案正確連結。

---

## 1. 標籤分層邏輯

雖然採用扁平結構（非層級式 `#Knowledge/Category`），但標籤在邏輯上分為三層：

### 第一層：檔案類型（必填）
檔案的身份標識，決定了檔案的角色。

| 標籤 | 使用檔案 | 說明 |
|------|---------|------|
| `#Summaries` | 01_Wiki/Summaries/ | 針對單一素材的摘要 |
| `#Concepts` | 01_Wiki/Concepts/ | 原子化的概念筆記 |

### 第二層：知識領域（可多選）
標示知識屬於哪個技術或業務領域，用於 Rule B 掃描時快速定位相關知識。

| 標籤 | 說明 | 典型概念 |
|------|------|---------|
| `#AI` | 人工智能相關 | RAG, LLMOps, Grounding 等 |
| `#Cloud` | 雲端基礎設施 | Serverless, Container, CloudRun 等 |
| `#Frontend` | 前端技術 | PWA, ServiceWorker, Web 等 |
| `#Productivity` | 生產力系統 | PARA, PAI, PKM 等 |
| `#Database` | 資料庫與並發 | Pessimistic Locking, Concurrency 等 |
| `#Fintech` | 金融科技 | 規則引擎, E-Commerce 等 |
| `#Infrastructure` | 通用基礎設施 | Container, Serverless, AWS 等 |
| `#Automation` | 工作流自動化 | n8n, Workflow Orchestration 等 |
| `#Security` | 安全與合規 | PII Scrubbing, Privacy, Compliance 等 |

### 第三層：具體工具或主題（可多選）
指向特定的工具、框架或技術主題，粒度最細。

| 標籤 | 說明 |
|------|------|
| `#Dify` | Dify 平台 |
| `#n8n` | n8n 工作流引擎 |
| `#LangChain` | LangChain 框架 |
| `#OpenClaw` | OpenClaw Agent 框架 |
| `#Docling` | Docling 文檔解析 |
| `#RAG` | 檢索增強生成技術 |
| `#LLMOps` | LLM 運維與觀察 |
| `#MCP` | Model Context Protocol |
| `#Workflow` | 工作流相關 |
| `#FinOps` | 成本治理 |
| `#Gateway` | API 閘道 |
| `#Grounding` | 事實接地 |
| `#Architecture` | 架構設計 |
| `#DataParsing` | 資料提取與解析 |
| `#Serverless` | 無伺服器運算 |
| `#Container` | 容器技術 |
| `#CloudRun` | Google Cloud Run |
| `#AppRunner` | AWS App Runner |
| `#AWS` | AWS 平台 |
| `#PWA` | 漸進式網頁應用 |
| `#ServiceWorker` | Service Worker 技術 |
| `#Web` | 網頁技術 |
| `#Mobile` | 行動應用 |
| `#AI-Agent` | AI Agent 框架 |
| `#KnowledgeManagement` | 知識管理系統 |
| `#Governance` | 治理框架 |

---

## 2. 命名規則

### 大小寫
- **必須 CamelCase**（首字母大寫）
  - ✅ `#RAG`, `#LLMOps`, `#Dify`
  - ❌ `#rag`, `#llmops`, `#dify`

### 連接符
- **多詞用連字符 `-`**（不用空格或 `/`）
  - ✅ `#AI-Agent`, `#AI-Engineering`, `#Data-Parsing`
  - ❌ `#AI/Agent`, `#AI Agent`, `#DataParsing`（除非是已確立的工具名）

### 避免的格式
- ❌ 層級符號：不用 `/` 分隔（如 `#Knowledge/Category`）
- ❌ 單數/複數混用：統一用 `#Summaries` 和 `#Concepts`
- ❌ 冗長標籤：避免超過 2-3 詞的組合
- ❌ 特殊符號：避免 `@`, `#`, `&` 等

---

## 3. 如何選擇標籤？

### 編譯新知識時的決策流程

```
開始編譯 Concept/Summary
    ↓
【第一層】加入檔案類型
    ├─ Summaries → 加 #Summaries
    └─ Concepts → 加 #Concepts
    ↓
【第二層】掃描內容，判斷知識領域（可多選）
    ├─ 涉及 AI/LLM？ → 加 #AI
    ├─ 涉及雲端基礎設施？ → 加 #Cloud
    ├─ 涉及前端？ → 加 #Frontend
    └─ ... 其他領域
    ↓
【第三層】確定具體工具/主題（可多選）
    ├─ 提到 Dify？ → 加 #Dify
    ├─ 涉及 RAG 技術？ → 加 #RAG
    └─ ... 其他具體主題
    ↓
完成（通常 2-5 個標籤）
```

### 舉例

**範例 1：「Dify 全方位知識白皮書」**
```
tags: #Summaries #AI #Dify #LLMOps #BaaS
└─ 檔案類型：#Summaries
└─ 知識領域：#AI
└─ 具體工具：#Dify, #LLMOps, #BaaS
```

**範例 2：「AI Agent Gateway」概念**
```
tags: #Concepts #AI #Governance #Gateway #FinOps #MCP
└─ 檔案類型：#Concepts
└─ 知識領域：#AI
└─ 具體主題：#Governance, #Gateway, #FinOps, #MCP
```

**範例 3：「Pessimistic Locking」概念**
```
tags: #Concepts #Database #Concurrency #Safety
└─ 檔案類型：#Concepts
└─ 知識領域：#Database
└─ 具體主題：#Concurrency, #Safety
```

---

## 4. 標籤與 Rule A & Rule B 的關係

### Rule A：編譯時（Concept → Project）
當編譯新 Concept 時，AI 會：
1. **掃描標籤**，理解此概念的知識領域和工具
2. **在 Concept 的 `## 🎯 關聯專案` 區塊**，連結至相關進行中的 Project Dashboard

### Rule B：更新時（Project → Concept）
當更新 Project Dashboard 時，AI 會：
1. **掃描 01_Wiki 中所有 Concepts/Summaries 的 tags**
2. **根據標籤與專案技術棧的匹配度**，填入 `## 🧠 相關 Wiki 概念` 區塊

因此，**標籤的準確性直接影響 Rule A & B 的效果**。

---

## 5. 標籤雲維護

### 什麼是標籤雲？
在 `01_Wiki/Main_Index.md` 的 `## 🏷️ 標籤雲` 區塊，維護出現 **2 次以上** 的標籤。

### 維護規則
- **何時更新**：執行「更新索引」指令時
- **來源**：掃描 `01_Wiki/Concepts/` 和 `01_Wiki/Summaries/` 的所有標籤
- **篩選條件**：只納入出現 2 次以上的標籤
- **目的**：提供知識庫內容的一覽，便於 Jason 快速了解知識覆蓋範圍

### 標籤雲示例
```markdown
## 🏷️ 標籤雲

`#RAG` `#AI` `#Dify` `#n8n` `#MCP` `#Docling` `#LangChain` 
`#FinOps` `#Security` `#PKM` `#Gateway` `#Grounding` `#OpenClaw` 
`#Serverless` `#Container` `#CloudRun` `#PWA` `#Frontend` `#ServiceWorker`
```

---

## 6. 常見問題

### Q: 為什麼要扁平結構而不是層級？
A: 扁平結構 (`#AI #Dify`) 比層級結構 (`#Knowledge/AI/Dify`) 更容易在 Obsidian 中掃描和聚合。Rule A & B 的邏輯是基於標籤的**並集**而非**樹狀關係**。

### Q: 新增工具時要怎麼辦？
A: 無需預先定義。當編譯含新工具的素材時，直接加入新標籤（遵循命名規則）。定期更新本文檔的「具體工具」清單即可。

### Q: 一個 Concept 要加多少個標籤？
A: **2-5 個**為最佳。
- 最少：1 個檔案類型 + 1 個領域 = 2 個
- 最多：1 個檔案類型 + 2-3 個領域 + 2-3 個具體主題 = 5-6 個
- 超過 6 個 = 信號異常，需重新評估

### Q: 如果一個 Concept 跨多個領域？
A: 多選。例如「AI 營運成本優化」同時涉及 AI、Infrastructure、FinOps：
```
tags: #Concepts #AI #Infrastructure #FinOps #Governance
```

---

## 7. 審計檢查清單

定期（如執行「系統健檢」時）檢查：

- [ ] 是否有 `#Summary` 單數形式存在？→ 改為 `#Summaries`
- [ ] 是否有層級標籤如 `#AI/Engineering`？→ 改為 `#AI-Engineering`
- [ ] 是否有超過 6 個標籤的檔案？→ 檢查是否標籤過度
- [ ] 標籤雲是否包含只出現 1 次的標籤？→ 移除
- [ ] 是否有新出現的標籤未納入本文檔？→ 更新本文檔

---

*最後更新：2026-05-10*
