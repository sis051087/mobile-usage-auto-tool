import pandas as pd
import os

# 輸出資料夾
os.makedirs("output_by_year", exist_ok=True)
os.makedirs("output_by_operator", exist_ok=True)

# 讀取CSV
df = pd.read_csv("input_data/行動寬頻用戶每月平均數據用量.csv")

df.columns = df.columns.str.strip()  # 去除空白

# 年月拆分
df["year"] = df["年月"].astype(str).str.split("/").str[0].astype(int)
df["month"] = df["年月"].astype(str).str.split("/").str[1].astype(int)

# 108～114 年
df = df[(df["year"] >= 108) & (df["year"] <= 114)]

for year in df["year"].unique():
    sub = df[df["year"] == year]
    sub.to_excel(f"output_by_year/usage_{year}.xlsx", index=False)
    print(f"已輸出：usage_{year}.xlsx")

# 輸出業者
operator_col = "業者名稱"

for op in df[operator_col].unique():
    sub = df[df[operator_col] == op]
    op_str = str(op)  # 轉成字串
    safe_name = op_str.replace("/", "_")
    sub.to_excel(f"output_by_operator/{safe_name}.xlsx", index=False)
    print(f"已輸出：{safe_name}.xlsx")

print("全部自動化報表輸出完成！")
