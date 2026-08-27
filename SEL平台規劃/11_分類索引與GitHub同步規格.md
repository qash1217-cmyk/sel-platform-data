# SEL 平台分類索引與 GitHub 同步規格

## 一、平台分類區塊

平台首頁建議設計為四個互相可連動的分類區塊：

1. **依資源類型**：評量工具與量表、教學活動與教案、學術文獻與實證、研習模組與講師素材。
2. **依 SEL 五大核心能力**：自我覺察、自我管理、社會覺察、人際關係、負責任的決定。
3. **依教育階段**：幼兒園、國小、國中、高中職、大專、跨教育階段。
4. **108 課綱相關資訊**：核心素養、學習領域、議題融入、學習表現、學習內容與課程融入建議。

四個區塊都應連到同一份主資料索引，點選任一分類後可繼續套用其他分類條件。例如：國小 → 人際關係 → 教學活動與教案 → 議題融入／品德教育。

## 二、資料檔案

- `12_SEL主分類索引.csv`：平台查詢用的主索引，每筆資料一列。
- `13_依資源類型索引.csv`：四種資源類型的篩選視圖。
- `14_依SEL五大能力索引.csv`：五大核心能力的篩選視圖。
- `15_依教育階段索引.csv`：教育階段的篩選視圖。
- `16_108課綱對應索引.csv`：108 課綱相關欄位的篩選視圖。
- `17_SEL分類索引.json`：前端或 API 使用的巢狀分類資料。

## 三、GitHub 建議目錄

```text
sel-platform-data/
├─ data/
│  ├─ resources.csv
│  ├─ classifications.csv
│  └─ generated/
├─ schemas/
│  └─ resource.schema.json
├─ docs/
│  └─ classification.md
└─ .github/workflows/
   └─ rebuild-sel-index.yml
```

本工作區已建立可直接搬移至上述結構的索引與 GitHub Actions 範例。Actions 會在主資料 CSV 變更時重新產生分類索引並建立工作流程摘要；是否自動 commit 回 repository，建議由正式 GitHub repository 的管理者決定。

## 四、主索引欄位

| 欄位 | 說明 |
|---|---|
| resource_id | 原始資源唯一識別碼 |
| resource_type | 四大資源類型之一 |
| sel_core_competency | SEL 五大核心能力之一；可用分號表示多重對應 |
| education_stage | 教育階段；可用分號表示多重對應 |
| curriculum_108_competency | 108 課綱核心素養，如 A1、B1、C2 |
| curriculum_108_area | 學習領域 |
| curriculum_108_issue | 議題融入 |
| curriculum_108_performance | 學習表現或課程表現描述 |
| curriculum_108_content | 學習內容或融入建議 |
| source_url | 原始來源 |
| verification_status | 查核狀態 |

## 五、108 課綱標記原則

108 課綱欄位分為「已明確對應」與「建議對應」兩種狀態。平台不得把依語意推估的對應標示成官方正式對應；須保留 `mapping_status`、`mapping_note` 與 `reviewer` 欄位，經課程專長教師或研究者審查後再改為推薦。

可先使用的跨領域核心素養標籤包括：自主行動、溝通互動、社會參與；實際 A／B／C 代碼與學習表現、學習內容應依教育階段、領域及課綱版本逐筆查核。

## 六、GitHub 連動方式

1. 建立 GitHub repository，將原始 CSV 放入 `data/resources.csv`。
2. 將 `tools/build_sel_indexes.py` 與 `.github/workflows/rebuild-sel-index.yml` 放入 repository。
3. 每次新增或修改資源後，執行 workflow 產生 4 個分類視圖與 JSON。
4. 平台前端讀取 `generated/17_SEL分類索引.json`，或由 API 提供查詢。
5. Pull Request 必須檢查來源、授權、查核狀態、108 課綱對應與個資欄位。

目前僅完成 GitHub-ready 的檔案與工作流程，尚未連線至特定遠端 repository。提供 repository URL 與授權方式後，才能進行實際 push 或 webhook 設定。


