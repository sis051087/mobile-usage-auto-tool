import pandas as pd
import os

# ====== 建立輸出資料夾 ======
os.makedirs("output_by_year", exist_ok=True)
os.makedirs("output_by_operator", exist_ok=True)

# ====== 讀取原始 CSV ======
df = pd.read_csv("input_data/行動寬頻用戶每月平均數據用量  (1).csv")

# ====== 清理欄位 ======
df.columns = df.columns.str.strip()  # 去除空白

# 年月欄位（114/9）拆成 年、月
df["year"] = df["年月"].astype(str).str.split("/").str[0]
df["month"] = df["年月"].astype(str).str.split("/").str[1]
# 年月拆分
df["year"] = df["年月"].astype(str).str.split("/").str[0].astype(int)
df["month"] = df["年月"].astype(str).str.split("/").str[1].astype(int)
# 🔥 只保留 108～114 年（你的專案時間範圍）
df = df[(df["year"] >= 108) & (df["year"] <= 114)]
# ====== 依年份自動輸出 ======
for year in df["year"].unique():
    sub = df[df["year"] == year]
    sub.to_excel(f"output_by_year/usage_{year}.xlsx", index=False)
    print(f"已輸出：usage_{year}.xlsx")

# ====== 依業者自動輸出 ======
operator_col = "業者名稱"

for op in df[operator_col].unique():
    sub = df[df[operator_col] == op]
    op_str = str(op)  # 轉成字串避免錯誤
    safe_name = op_str.replace("/", "_")
    sub.to_excel(f"output_by_operator/{safe_name}.xlsx", index=False)
    print(f"已輸出：{safe_name}.xlsx")

print("全部自動化報表輸出完成！")