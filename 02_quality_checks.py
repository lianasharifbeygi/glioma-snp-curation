import pandas as pd
import numpy as np

# خواندن فایل‌های تمیز
df1 = pd.read_csv("data/cleaned_susceptibility.csv")
df2 = pd.read_csv("data/cleaned_pharmacogenetics.csv")
df3 = pd.read_csv("data/cleaned_needs_review.csv")

dfs = {
    "susceptibility": df1,
    "pharmacogenetics": df2,
    "needs_review": df3
}

print("========== گزارش کنترل کیفیت ==========\n")

for name, df in dfs.items():
    print(f"--- فایل: {name} ---")
    print(f"تعداد ردیف: {len(df)}")
    
    # تعداد مقادیر خالی در چند ستون مهم
    important_cols = ["Cases", "controls", "Total_Sample_Size", "Effect_Size", "P_Value", "Beta_lnOR"]
    for col in important_cols:
        if col in df.columns:
            missing = df[col].isna().sum()
            print(f"  مقادیر خالی در {col}: {missing}")
    
    # بررسی Cases + controls ≈ Total_Sample_Size
    if all(c in df.columns for c in ["Cases", "controls", "Total_Sample_Size"]):
        temp = df[["Cases", "controls", "Total_Sample_Size"]].apply(pd.to_numeric, errors="coerce")
        diff = (temp["Cases"] + temp["controls"] - temp["Total_Sample_Size"]).abs()
        mismatch = (diff > 1).sum()  # اختلاف بیشتر از 1
        print(f"  تعداد ردیف با ناسازگاری Cases+controls و Total: {mismatch}")
    
    print()

print("کنترل کیفیت تمام شد.")