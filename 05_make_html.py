import pandas as pd

# خواندن سه فایل
try:
    df1 = pd.read_csv("data/cleaned_susceptibility.csv")
    df2 = pd.read_csv("data/cleaned_pharmacogenetics.csv")
    df3 = pd.read_csv("data/cleaned_needs_review.csv")
except FileNotFoundError:
    df1 = pd.read_csv("cleaned_susceptibility.csv")
    df2 = pd.read_csv("cleaned_pharmacogenetics.csv")
    df3 = pd.read_csv("cleaned_needs_review.csv")

df1["Dataset"] = "Susceptibility"
df2["Dataset"] = "Pharmacogenetics"
df3["Dataset"] = "Needs Review"

df = pd.concat([df1, df2, df3], ignore_index=True)

# نمایش علمی برای P_Value
if "P_Value" in df.columns:
    def format_pval(x):
        try:
            val = float(x)
            if val == 0 or pd.isna(val):
                return "NR"
            return f"{val:.2e}"
        except:
            return str(x)
    df["P_Value"] = df["P_Value"].apply(format_pval)

cols = ["rsID", "Gene", "Subtype", "Risk_Effect_Allele", "Effect_Measure",
        "Effect_Size", "P_Value", "Evidence_Tier", "Dataset"]
cols = [c for c in cols if c in df.columns]

table_html = df[cols].to_html(index=False, classes="snp-table", border=0, na_rep="NR")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Glioma SNP Database</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 40px; background: #f7f7f7; }}
    h1 {{ color: #333; }}
    p {{ color: #555; }}
    table {{ border-collapse: collapse; width: 100%; background: white; font-size: 13px; }}
    th, td {{ border: 1px solid #ddd; padding: 6px 8px; text-align: left; }}
    th {{ background-color: #4C72B0; color: white; position: sticky; top: 0; }}
    tr:nth-child(even) {{ background-color: #f2f2f2; }}
  </style>
</head>
<body>
  <h1>Glioma-Associated SNP Database</h1>
  <p>Total SNPs: {len(df)} | Susceptibility: {len(df1)} | Pharmacogenetics: {len(df2)} | Needs Review: {len(df3)}</p>
  {table_html}
  <p style="margin-top:30px;color:#888;font-size:13px;">Undergraduate mini-project | glioma-snp-curation</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("فایل index.html با P_Value اصلاح‌شده ساخته شد.")