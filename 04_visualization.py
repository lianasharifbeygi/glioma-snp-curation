import pandas as pd
import matplotlib.pyplot as plt
import os

# ساخت پوشه برای ذخیره نمودارها
os.makedirs("figures", exist_ok=True)

# خواندن فایل‌ها
df1 = pd.read_csv("data/cleaned_susceptibility.csv")
df2 = pd.read_csv("data/cleaned_pharmacogenetics.csv")
df3 = pd.read_csv("data/cleaned_needs_review.csv")

# ---------- نمودار ۱: تعداد SNP بر اساس Tier ----------
tier_counts = pd.concat([
    df1["Evidence_Tier"],
    df2["Evidence_Tier"],
    df3["Evidence_Tier"]
]).value_counts()

plt.figure(figsize=(7, 5))
tier_counts.plot(kind="bar", color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Number of SNPs by Evidence Tier")
plt.xlabel("Evidence Tier")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("figures/snp_by_tier.png", dpi=150)
plt.close()

# ---------- نمودار ۲: تعداد SNP بر اساس Subtype (فقط susceptibility) ----------
if "Subtype" in df1.columns:
    subtype_counts = df1["Subtype"].value_counts().head(10)  # ۱۰ تای اول

    plt.figure(figsize=(9, 6))
    subtype_counts.plot(kind="barh", color="#4C72B0")
    plt.title("Top Subtypes in Susceptibility SNPs")
    plt.xlabel("Count")
    plt.ylabel("Subtype")
    plt.tight_layout()
    plt.savefig("figures/snp_by_subtype.png", dpi=150)
    plt.close()

# ---------- نمودار ۳: مقایسه سه فایل ----------
file_counts = {
    "Susceptibility": len(df1),
    "Pharmacogenetics": len(df2),
    "Needs Review": len(df3)
}

plt.figure(figsize=(7, 5))
plt.bar(file_counts.keys(), file_counts.values(), color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Number of SNPs in Each Dataset")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("figures/snp_by_dataset.png", dpi=150)
plt.close()

print("نمودارها ساخته شدند و در پوشه figures ذخیره شدند.")