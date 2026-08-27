# 01｜SEL 資料庫／教師專業發展平台建置進度與接續筆記

> 建立日期：2026-08-27
> 
> 專案名稱：SEL 教師專業發展平台／資料庫
> 
> GitHub：<https://github.com/qash1217-cmyk/sel-platform-data>
> 
> 公開網站：<https://qash1217-cmyk.github.io/sel-platform-data/>

## 一、專案目標

建置一個以臺灣教育現場為核心的 SEL（Social and Emotional Learning，社會情緒學習）教師專業學習與實踐支持平台。

平台不是單純的教材下載網站，而是支持以下循環：

```text
理解 SEL 概念 → 搜尋資源 → 備課／改編 → 課堂實施 → 教師反思 → 同儕共備 → 累積案例
```

主要服務對象包括一般教師、導師、科任教師、輔導教師、行政人員、教師專業學習社群、師培者、研究者與教育主管機關。

## 二、目前完成成果

### 1. 第一批資源資料

- 已建立第一批 100 筆 SEL 資源建庫種子資料。
- 資源涵蓋國際框架、研究、政策、教師專業、教學策略、案例、評量與網站入口。
- 每筆資料保留唯一識別碼，例如 `SEL-001`；前台不再只顯示編號，而是顯示完整資源名稱。
- 部分資料是官方入口或候選索引，不應誤視為已完成全文、授權、研究與信效度查核的教材。

### 2. 四大資源類型

目前統一分類為：

1. 評量工具與量表
2. 教學活動與教案
3. 學術文獻與實證
4. 研習模組與講師素材

### 3. SEL 五大核心能力

平台已建立五大能力分類與說明：

- 自我覺察：辨識自己的情緒、想法、價值、優勢與限制，理解其如何影響行為與選擇。
- 自我管理：調節情緒、想法與行為，管理壓力、設定目標並持續行動。
- 社會覺察：理解他人的觀點與感受，展現同理並理解家庭、學校與社會脈絡。
- 人際關係：建立與維持健康關係，包含溝通、傾聽、合作、協商、衝突處理與求助。
- 負責任的決定：依據倫理、安全、規範與可能後果，做出兼顧自己與他人的建設性選擇。

每項能力目前另有「教師觀察重點」與「課堂切入方式」。

### 4. 教育階段

目前支援：幼兒園、國小、國中、高中職、大專與跨教育階段。多教育階段資源以分號保存，例如 `國小;國中`。

### 5. 108 課綱

資料模型已預留以下欄位：

- 108 課綱核心素養
- 學習領域
- 議題融入
- 學習表現
- 學習內容
- 對應說明
- 對應狀態與審查者

目前資料中的部分 108 課綱代碼與對應是「建議對應／待審查」，不可直接宣稱為官方正式對應。後續應依教育階段、學習領域與課綱文件逐筆確認。

## 三、資料檔案清單

所有主要檔案位於本資料夾內的 `SEL平台規劃` 子資料夾。

### 規劃與研究文件

- `SEL平台規劃/00_執行摘要.md`
- `SEL平台規劃/01_國內外資源清單.md`
- `SEL平台規劃/02_資料庫欄位規格.md`
- `SEL平台規劃/03_平台功能需求書.md`
- `SEL平台規劃/04_教師使用者旅程.md`
- `SEL平台規劃/05_MVP系統架構圖.md`
- `SEL平台規劃/06_內容種子與審查流程.md`

### 原始與分類資料

- `SEL平台規劃/07_第一批100筆資源.csv`：原始 100 筆建庫資料。
- `SEL平台規劃/12_SEL主分類索引.csv`：主分類索引。
- `SEL平台規劃/13_依資源類型索引.csv`：四大資源類型視圖。
- `SEL平台規劃/14_依SEL五大能力索引.csv`：五大核心能力視圖。
- `SEL平台規劃/15_依教育階段索引.csv`：教育階段視圖。
- `SEL平台規劃/16_108課綱對應索引.csv`：108 課綱相關視圖。
- `SEL平台規劃/17_SEL分類索引.json`：前端使用的分類與資源 ID 索引。
- `SEL平台規劃/18_SEL資源摘要索引.json`：每筆資源的名稱、平台摘要、分類、教育階段、來源與查核狀態。
- `SEL平台規劃/19_SEL五大核心能力說明.json`：五大能力定義、教師觀察與課堂切入資料。
- `SEL平台規劃/20_影音與網站資源.json`：影音／網站資源索引，目前 10 筆。

### 試點與回饋

- `SEL平台規劃/08_試點教師回饋表.md`：試點教師前測、使用後問卷與開放題。
- `SEL平台規劃/09_試點回饋後功能調整矩陣.md`：回饋問題、優先級、功能調整與驗收方式。

### 圖表與報告

- `SEL平台規劃/10_SEL圖表數據_APA7.docx`：APA 7 格式 Word 報告。
- `SEL平台規劃/10_SEL圖表數據彙整.json`：圖表彙整資料。
- `SEL平台規劃/10_圖1_資源類型.png`
- `SEL平台規劃/10_圖2_資源來源.png`
- `SEL平台規劃/10_圖3_查核狀態.png`

## 四、資料模型與欄位決策

### 資源主體欄位

主要欄位包括：

- `resource_id`
- `title`
- `abstract_summary`
- `medium`
- `resource_type`
- `sel_core_competency`
- `education_stage`
- `curriculum_108_competency`
- `curriculum_108_area`
- `curriculum_108_issue`
- `curriculum_108_performance`
- `curriculum_108_content`
- `mapping_status`
- `source`
- `source_url`
- `verification_status`
- `license_or_access`
- `notes`

### 摘要規則

目前 `abstract_summary` 已從「說明它屬於哪一類、對應哪一能力、適用哪個階段」改為針對資源內容本身的摘要，例如說明其研究架構、教學方法、政策內容、學校實施方式或教師研習用途。

分類、能力與教育階段資訊改放在摘要下方的 metadata 區域。

目前摘要多為「平台整理摘要」，不是直接擷取原文摘要。後續若取得正式論文或影音逐字稿，建議增加：

- `original_abstract`
- `platform_summary`
- `abstract_language`
- `abstract_source`
- `abstract_verified`

## 五、平台前端設計現況

公開首頁位於 repository 根目錄的 `index.html`。

### 視覺風格

- 文青、安靜、閱讀型介面。
- 米白／淡紫灰背景。
- 莫蘭迪藍紫色為主色，搭配低飽和灰紫、暖棕點綴。
- 使用手寫／楷書風格字體 fallback：`LXGW WenKai`、`Kaiti TC`、`DFKai-SB`、`標楷體`。
- 資源以紙張感卡片呈現。

### 版面配置

- 左側固定分類側欄。
- 分類選項不放在上方。
- 左側包含：
  - 依資源類型
  - 依 SEL 五大核心能力
  - 依教育階段
  - 108 課綱相關資訊
- 主畫面包含：
  - 平台介紹
  - 關鍵字搜尋
  - 資料總數統計
  - SEL 五大核心能力介紹
  - 純文獻與文字資料
  - 影音與網站資源

### 資源卡片

每張卡片目前顯示：

- 完整資源名稱
- 平台整理摘要
- 資源類型
- 教育階段
- 查核狀態
- 原始來源連結

## 六、影音與網站資源

已建立 `20_影音與網站資源.json`，目前包含 CASEL、Yale RULER、Harvard EASEL、OECD、EEF、UNESCO、美國教育部、臺灣教育部及全國教師在職進修資訊網等入口。

重要原則：

- 官方入口不等於直接影片網址。
- 「待影片頁面查核」的資料只能作為搜尋入口或候選索引。
- 後續應補上直接影片 URL、影片標題、講者、日期、長度、字幕、語言、授權、逐字稿與摘要。
- 影音資源與純文獻／文字資料在首頁分成兩個區塊。

建議後續為影音資料增加欄位：

```text
media_kind
video_url
platform
speaker
published_at
duration_seconds
language
has_subtitles
transcript_url
media_license
media_summary
```

## 七、GitHub 部署狀況

### Repository

<https://github.com/qash1217-cmyk/sel-platform-data>

- 公開 repository。
- 預設分支：`main`。
- 已部署規劃文件、資料 CSV、分類 JSON、前端首頁、工具程式與 workflow。

### GitHub Actions

已建立：

- `.github/workflows/rebuild-sel-index.yml`
- `.github/workflows/deploy-pages.yml`

`rebuild-sel-index.yml`：

- 監看主資源 CSV 與分類工具。
- 重新產生四種分類 CSV、分類 JSON、資源摘要 JSON。
- 目前也包含五大核心能力說明與影音資源索引作為 workflow artifact。

`deploy-pages.yml`：

- 監看 `main` 分支。
- 使用 GitHub Pages artifact 部署根目錄網站。
- 權限設定為 `contents: read`、`pages: write`、`id-token: write`。

### 部署紀錄

最新一次成功部署：

<https://github.com/qash1217-cmyk/sel-platform-data/actions/runs/33049221758>

分類索引重建最近成功執行，之後首頁風格與影音區塊更新也已成功部署。

### 公開網站

<https://qash1217-cmyk.github.io/sel-platform-data/>

如果更新後看不到內容，先等待 GitHub Pages 快取更新，再用 `Ctrl + F5` 重新整理。

## 八、重要修正歷程

### 1. 從編號顯示改為資源名稱

最初分類 JSON 只回傳 `SEL-001` 等 ID，前台看不到文獻名稱。後續新增 `18_SEL資源摘要索引.json`，前台改以資源完整名稱顯示，ID 只作為資料庫識別碼。

### 2. 摘要內容修正

最初摘要會說明「此資源屬於哪種分類、聚焦哪項能力、適用哪個階段」，不符合文獻摘要需求。後續已改為依標題、來源與資源內容寫平台整理摘要，分類資訊改放 metadata。

### 3. 五大核心能力獨立說明

五大能力不再只作為篩選標籤，而是建立獨立 JSON 與首頁說明區，內容包含定義、教師觀察重點與課堂切入方式。

### 4. 純文獻與影音／網站分區

首頁已分成「純文獻與文字資料」及「影音與網站資源」兩個區塊，並新增影音／網站索引。

### 5. 介面風格調整

原本較接近一般資料平台，後續改為文青閱讀風格，分類移至左側，並改用藍紫色莫蘭迪配色與手寫／楷書 fallback 字體。

### 6. GitHub Pages 部署問題

第一次部署曾因 GitHub Pages 尚未啟用而失敗。使用者在 repository Settings → Pages 將 Source 設為 GitHub Actions 後，重新執行部署已成功。

## 九、目前已知限制

1. 影音索引仍有部分是官方入口，不是直接影片頁面。
2. 100 筆資料中有許多項目仍待直接頁面、授權、研究證據或信效度查核。
3. 108 課綱欄位目前多為建議對應，尚未逐筆完成課程專長審查。
4. 前台搜尋目前是 JSON 載入後的簡易文字搜尋，尚未真正做到多條件交集篩選。
5. 左側分類目前點選一個分類後顯示該分類結果，尚未保留多個分類條件的交叉選取狀態。
6. Word 報告目前在本地產製，尚未整合到 GitHub Pages 的線上匯出服務。
7. 試點教師回饋表已建立，但尚未有真實試點回饋資料，因此功能優先級仍有假設成分。
8. 尚未建立後端資料庫、帳號、登入、教師學習歷程、權限管理與個資隔離服務。

## 十、下一階段優先工作

### 優先級 P0：內容可信度與可用性

- 逐筆查核 100 筆資源的直接網址與頁面狀態。
- 補齊作者／機構、年份、正式標題與出版資訊。
- 補齊授權與可否下載、改編、翻譯、再分享。
- 把平台整理摘要與正式原文摘要分開保存。
- 逐筆檢核 108 課綱對應，移除未經確認的官方語氣。

### 優先級 P1：影音資料

- 實際搜尋與登錄 20–30 筆直接影音資源。
- 補上影片標題、講者、日期、長度、字幕、語言與授權。
- 為影音建立獨立摘要與逐字稿欄位。
- 在前台增加影片縮圖、長度、字幕與觀看平台標籤。

### 優先級 P1：搜尋與分類體驗

- 實作多條件交集篩選：資源類型 × 核心能力 × 教育階段 × 108 課綱。
- 加入「清除篩選」與目前條件 chips。
- 顯示分類結果的筆數與無結果建議。
- 針對手機版優化左側分類，改為可展開抽屜。

### 優先級 P1：試點驗證

- 以 3–5 所學校、10–20 位教師進行任務測試。
- 測試任務：搜尋、閱讀摘要、找到可用教案、查看影音、下載資料、完成反思。
- 依回饋更新 `09_試點回饋後功能調整矩陣.md`。
- 不以教師個人排名為分析方式。

### 優先級 P2：正式平台化

- 建立後端 API 與正式資料庫。
- 加入教師／學校／審查者／管理者權限。
- 建立內容審查、版本控制、稽核與複審提醒。
- 整合教師研習系統或單一登入。
- 建立個資最小化、去識別化與研究資料隔離機制。

## 十一、下一個 session 建議開場指令

可將以下內容貼給下一個 session：

> 請讀取 `01_SEL資料庫平台建置進度與接續筆記.md`，並檢查 GitHub repository `qash1217-cmyk/sel-platform-data` 的目前狀態。接續完成 P0／P1 工作，先確認 100 筆資源的直接網址、正式摘要、授權與 108 課綱對應，再優化多條件交叉篩選與影音資源資料。不要虛構尚未取得的試點回饋或文獻摘要；所有待查項目請保留查核狀態。

## 十二、接續時的注意事項

- 不要把 `resource_id` 當作前台主要顯示名稱。
- 不要把平台整理摘要標示為原文摘要。
- 不要把官方入口標示為已確認的直接影音檔。
- 不要把建議的 108 課綱對應標示為官方正式對應。
- 不要在一般資源庫保存學生可識別的心理、輔導或個案資料。
- 不要使用教師個人 SEL 評量進行排名或績效考核。
- 更新 GitHub 上既有檔案前先取得目前 blob SHA，避免覆寫他人變更。
- 修改主 CSV 後確認兩個 GitHub Actions 均成功。

## 十三、Firebase 後台資料庫建置狀態（2026-08-27）

Firebase 專案：`sel-database-2a325`

已在本地與 GitHub 建立 Firebase 後台部署骨架：

- `firebase.json`：Firestore 與 Functions 設定。
- `firestore.rules`：前台只讀取 `published`；編輯者可建立／修改；管理者可刪除；審查者管理 `reviews`；使用者角色使用 custom claims。
- `firestore.indexes.json`：資源類型、教育階段、SEL 能力與影音查詢索引。
- `functions/index.js`：已規劃已發布資源搜尋、設定使用者角色、資源異動 audit log。
- `functions/package.json`：Firebase Functions Node 20 依賴。
- `tools/seed_firestore.js`：將 100 筆資源、5 筆核心能力、10 筆影音／網站資料匯入 Firestore；預設全部為 `draft`。
- `firebase/README.md`：部署、匯入、權限與安全說明。

目前尚未實際執行 Firebase deploy 或 Firestore seed，原因是工作區沒有 Firebase CLI、服務帳號或可直接操作 Firebase 的連接器。不可把目前狀態稱為「Firebase 已上線」；目前是「Firebase-ready 後台程式與規則已建立」。

實際部署需要：

1. 安裝 Firebase CLI。
2. 對 `sel-database-2a325` 執行 `firebase login`。
3. 啟用 Firestore、Authentication 與 Cloud Functions。
4. 設定 `GOOGLE_APPLICATION_CREDENTIALS`，但不可把 service-account JSON 放入 GitHub。
5. 執行 `firebase deploy --only firestore:rules,firestore:indexes,functions`。
6. 執行 `node tools/seed_firestore.js`。
7. 以 Firebase Console 檢查 3 個集合是否建立：`resources`、`competencies`、`mediaResources`。

下一階段應建立管理後台頁面，提供資源新增、編輯、草稿／送審／發布、影音資料管理、審查紀錄、版本比較與 audit log 查詢。正式接前台前，必須取得 Firebase Web App config，並將前台靜態 JSON 改為讀取 Firebase Functions 或 Firestore 的 `published` 資料。

