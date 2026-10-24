import pandas as pd

# خواندن فایل‌های تمیز
df1 = pd.read_csv("data/cleaned_susceptibility.csv")
df2 = pd.read_csv("data/cleaned_pharmacogenetics.csv")
df3 = pd.read_csv("data/cleaned_needs_review.csv")

print("========== تحلیل پایه ==========\n")

# ----- فایل susceptibility -----
print("--- susceptibility ---")
print(f"تعداد کل SNP: {len(df1)}")

if "Evidence_Tier" in df1.columns:
    print("\nتعداد بر اساس Evidence_Tier:")
    print(df1["Evidence_Tier"].value_counts())

if "Subtype" in df1.columns:
    print("\nتعداد بر اساس Subtype:")
    print(df1["Subtype"].value_counts())

if "Population_Ethnicity" in df1.columns:
    print("\nتعداد بر اساس Population:")
    print(df1["Population_Ethnicity"].value_counts())

print("\n")

# ----- فایل pharmacogenetics -----
print("--- pharmacogenetics ---")
print(f"تعداد کل SNP: {len(df2)}")

if "Evidence_Tier" in df2.columns:
    print("\nتعداد بر اساس Evidence_Tier:")
    print(df2["Evidence_Tier"].value_counts())

if "Effect_Measure" in df2.columns:
    print("\nتعداد بر اساس Effect_Measure:")
    print(df2["Effect_Measure"].value_counts())

print("\n")

# ----- فایل needs_review -----
print("--- needs_review ---")
print(f"تعداد کل SNP: {len(df3)}")

if "Evidence_Tier" in df3.columns:
    print("\nتعداد بر اساس Evidence_Tier:")
    print(df3["Evidence_Tier"].value_counts())

print("\nتحلیل پایه تمام شد.")