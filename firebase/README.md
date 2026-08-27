# Firebase 後台資料庫建置說明

專案：`sel-database-2a325`

## 已建立的後台集合

- `resources`：純文獻與文字資源。
- `mediaResources`：影音與網站資源。
- `competencies`：SEL 五大核心能力定義、教師觀察重點與課堂切入方式。
- `categories`：資源類型、教育階段與 108 課綱分類設定。
- `reviews`：內容、教學、文化／心理安全與版權審查。
- `auditLogs`：資源異動紀錄，只允許新增，不允許修改或刪除。
- `users`：使用者角色與偏好。

## 資源狀態

`draft` → `review` → `published` → `archived`

匯入工具預設全部建立為 `draft`，管理者審查後才能發布；前台只讀取 `published`。

## 部署前需求

1. 安裝 Firebase CLI 並執行 `firebase login`。
2. 確認帳號具有 `sel-database-2a325` 的 Firebase／Firestore 管理權限。
3. 在 Firebase Console 啟用 Firestore、Authentication 與 Cloud Functions。
4. 依最小權限建立 service account，將 JSON 路徑放入 `GOOGLE_APPLICATION_CREDENTIALS`；不要把 JSON 放入 GitHub。
5. 執行 `firebase use sel-database-2a325`。
6. 執行 `firebase deploy --only firestore:rules,firestore:indexes,functions`。
7. 執行 `node tools/seed_firestore.js`，將目前資料以 `draft` 狀態匯入。

## 安全原則

- 不把 Firebase service-account JSON、私鑰或管理員 token 上傳 GitHub。
- Firestore Security Rules 已將前台讀取限制為 `published`。
- 編輯、審查與管理權限使用 Firebase Authentication custom claims。
- 學生個別心理、輔導與可識別資料不放入一般資源集合。
- 所有內容異動由 Cloud Function 寫入 `auditLogs`。


