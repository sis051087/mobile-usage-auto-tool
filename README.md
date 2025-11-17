# 行動寬頻用戶數據自動分類與報表生成工具（Python 自動化）

本專案透過 Python 自動化處理「行動寬頻用戶每月平均數據用量」資料，
能自動將原始 CSV 檔依 **年份** 與 **電信業者** 自動切分，並輸出乾淨的 Excel 報表。

此專案模擬真實企業常見的資料處理流程，可應用於：
- 月報／年報自動化
- 部門資料分檔
- 大量資料清理與拆分
- 自動產生多份報表

## 目錄
- [專案結構](#專案結構)
- [使用技術](#使用技術)
- [原始資料來源](#原始資料來源)
- [使用方式](#使用方式)
- [程式輸出結果](#程式輸出結果)
- [執行成果截圖](#執行成果截圖)
- [專案亮點](#專案亮點)
- [作者](#作者)


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

### 1. 將資料放入 `input_data/`

請將下載的 CSV 檔放入：input_data/
例如：input_data/行動寬頻用戶每月平均數據用量.csv
---

### 2. 安裝套件
pip install pandas openpyxl
---

### 3. 執行程式
python main.py
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

<img width="441" height="143" alt="截圖 2025-11-17 晚上7 25 12" src="https://github.com/user-attachments/assets/2114b4b3-12d4-4940-8af2-ef2d58028b3e" />

<img width="351" height="198" alt="截圖 2025-11-17 晚上7 20 03" src="https://github.com/user-attachments/assets/3c8f425a-87a9-4042-a395-771ef3ab10a3" />

<img width="393" height="220" alt="截圖 2025-11-17 晚上7 20 31" src="https://github.com/user-attachments/assets/78256621-f74d-4c45-9345-2c64f67740eb" />

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
