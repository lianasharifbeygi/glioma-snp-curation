import pandas as pd

# خواندن سه فایل
df1 = pd.read_excel("data/glioma_susceptibility.xlsx")
df2 = pd.read_excel("data/glioma_pharmacogenetics.xlsx")
df3 = pd.read_excel("data/needs_evidence_review.xlsx")

# تبدیل مقادیر خالی و متن‌های شبیه خالی به NA
for df in [df1, df2, df3]:
    df.replace(["", " ", "NR", "NA", "N/A", "None", "~"], pd.NA, inplace=True)

# ذخیره نسخه تمیز
df1.to_csv("data/cleaned_susceptibility.csv", index=False)
df2.to_csv("data/cleaned_pharmacogenetics.csv", index=False)
df3.to_csv("data/cleaned_needs_review.csv", index=False)

print("تمیزسازی انجام شد.")