# 行動寬頻用戶數據自動分類與報表生成工具（Python 自動化）

本專案透過 Python 自動化處理「行動寬頻用戶每月平均數據用量」資料，
能自動將原始 CSV 檔依 **年份** 與 **電信業者** 自動切分，並輸出乾淨的 Excel 報表。

此專案模擬真實企業常見的資料處理流程，可應用於：
- 月報／年報自動化
- 部門資料分檔
- 大量資料清理與拆分
- 自動產生多份報表

---

## 📁 專案結構

mobile_usage_auto_tool/

│── main.py

│── input_data/               ← 放原始資料（CSV）

│── output_by_year/           ← 程式執行後自動產生

│── output_by_operator/       ← 程式執行後自動產生

│── README.md

---

## 🔧 使用技術（Tech Stack）

- Python 3
- Pandas
- openpyxl
- 自動化資料處理流程

---

## 📊 原始資料來源

資料集：行動寬頻用戶每月平均數據用量  
來源：政府資料開放平台 (data.gov.tw)  
網址：https://data.gov.tw/dataset/30770

---

## ▶️ 使用方式

### 1. 安裝必要套件
```
pip install -r requirements.txt
```

requirements.txt 內容：
```
pandas
```

### 2. 執行程式
```
python main.py
```
---

## 📂 程式輸出結果（執行後自動生成）

### ✔ 依年份輸出（output_by_year/）
usage_108.xlsx

usage_109.xlsx

…

usage_114.xlsx
### ✔ 依電信業者輸出（output_by_operator/）

中華電信股份有限公司.xlsx

遠傳電信股份有限公司.xlsx

台灣大哥大股份有限公司.xlsx

台灣之星電信股份有限公司.xlsx

---

## 📸 執行成果截圖

![終端機執行畫面](image/terminal.png)

![年份輸出的結果資料夾](image/output_year.png)

![業者輸出的結果資料夾](image/output_operator.png)

---

## 🧩 專案亮點

- 完整資料處理流程（清理 → 拆分 → 輸出）
- 具備再現性（任何人跑 main.py 都能得到結果）
- 此專案符合企業常見需求（自動化報表生成）
- 程式碼簡潔且可讀性高

---

## 🙋‍♂️ 作者

陳柏瀚 Jim Chen 
GitHub: https://github.com/sis051087
