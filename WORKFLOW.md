# Project Workflow

This document describes the full workflow of the glioma SNP curation project, from SNP discovery to the final HTML database.

---

## 1. Project Scope

- Primary phenotype: Glioma (with subtypes such as GBM, Non-GBM, IDH-mutated, etc.)
- Target: high-quality curated SNPs (not forced to 100 low-quality entries)
- Final curated set: 52 SNPs
- Evidence tiers:
  - Tier1: strong GWAS / meta-analysis support
  - Tier2: pharmacogenetic / candidate / prognosis-related
  - Tier3: population-specific (mainly East Asian) associations

---

## 2. SNP Discovery and Source Selection

Main sources used:

- GWAS Catalog
- PubMed / Europe PMC (key papers: Shete 2009, Wrensch 2009, Sanson 2011, Melin 2017, Eckel-Passow 2020, and selected pharmacogenetic studies)
- dbSNP / Ensembl for genomic annotation
- Secondary tables from reviews when needed for allele frequency or sample size context

Search focus:

- Glioma / glioblastoma susceptibility GWAS
- Subtype-specific loci (GBM vs Non-GBM, IDH status)
- Pharmacogenetics of temozolomide (TMZ) response, survival, and toxicity

---

## 3. Column Schema (Full Annotation Table)

Each SNP was annotated with the following columns:

| Column | Description |
|--------|-------------|
| rsID | SNP identifier |
| Gene | Gene or nearest locus |
| Phenotype | Main phenotype (Glioma / Glioblastoma) |
| Subtype | Molecular or histological subtype |
| Reference_Allele | Reference allele (GRCh38-oriented when possible) |
| Alternative_Allele | Alternative allele |
| Risk_Effect_Allele | Reported risk / effect allele |
| Risk_Allele_Frequency_in_Controls | RAF in controls (if reported) |
| Risk_Allele_Frequency_in_Cases | RAF in cases (if reported) |
| Study_Reported_RAF | RAF as reported in the primary study |
| Genome_Assembly | GRCh38 coordinate window (101 bp) |
| Population_Ethnicity | Study population |
| Cases | Number of cases |
| controls | Number of controls |
| Total_Sample_Size | Cases + controls (or study/analysis total) |
| Effect_Measure | OR or HR |
| Effect_Size | Reported effect size |
| P_Value | Association p-value |
| PMID | Primary publication ID |
| Sex_Related | Sex-specific notes |
| Age_Related | Age-related notes |
| Environmental_Factor | e.g. TMZ exposure |
| Beta_lnOR | ln(OR) when Effect_Measure = OR; left empty for HR |
| FASTA | 101 bp sequence (50 bp upstream + SNP + 50 bp downstream) |
| Source_Database | Main source label |
| Original_Source_Link | Original combined link(s) |
| PubMed_Link | Direct PubMed URL |
| dbSNP_Link | Direct dbSNP URL |
| Evidence_Type | GWAS / pharmacogenetic / candidate |
| QC_Status | PARTIAL / NEEDS_REVIEW |
| Notes | Important caveats (strand, subtype N, mixed evidence) |
| Citation_Source | EuropePMC (consistent source) |
| Citation_Count | Citation count from EuropePMC |
| Extraction_Date | 2026-10-10 |
| Study_Reference | Short citation (Author Year Journal) |
| Evidence_Tier | Tier1 / Tier2 / Tier3 |

---

## 4. Data Extraction Rules

### Alleles and strand
- Genomic alleles checked against dbSNP/Ensembl (GRCh38).
- When GWAS risk allele did not match genomic alleles (e.g. rs2736100), the mismatch was documented in Notes.

### FASTA
- Fixed rule for all SNPs: 101 bp total
- Format: 50 bp before SNP + 1 bp at SNP position + 50 bp after
- SNP is always at position 51 of the sequence

### Sample sizes
- For full-study associations: discovery or meta-analysis totals used
- For subtype-specific Melin 2017 analyses:
  - GBM analysis total ≈ 24381 (6191 cases + 18190 controls)
  - Non-GBM analysis total ≈ 24009 (5819 cases + 18190 controls)
- Full study total (30686) kept in Notes when relevant

### Effect sizes
- OR → Beta_lnOR = ln(OR)
- HR → Beta_lnOR left empty (column reserved for ln(OR) only)

### Citation counts
- All taken from EuropePMC on the same date (2026-10-10) for consistency

---

## 5. Quality Control During Curation

Manual checks included:

- Matching rsID ↔ gene ↔ PMID
- Consistency of Cases + controls with Total_Sample_Size
- Correct PubMed and dbSNP links
- Strand / allele orientation notes
- Avoiding mixing ORs from different studies for the same SNP without documentation
- Separating susceptibility evidence from pharmacogenetic evidence

QC_Status meanings:

- **PARTIAL**: core fields filled; full paper-by-paper verification not completed for every field
- **NEEDS_REVIEW**: special issues remain (e.g. strand orientation)

---

## 6. Splitting the Master Table

The master table (52 SNPs) was split into three analysis-ready files:

1. **glioma_susceptibility** (40 SNPs)
   - Tier1 GWAS loci + Tier3 population-specific risk loci
2. **glioma_pharmacogenetics** (8 SNPs)
   - TMZ response, survival, toxicity-related variants
3. **needs_evidence_review** (4 SNPs)
   - Candidate associations with mixed or weaker evidence

This separation keeps risk-association analyses distinct from treatment-response analyses.

---

## 7. Computational Pipeline (Reproducible Steps)

### 7.1 Environment

    pip install pandas openpyxl matplotlib

### 7.2 Data cleaning

    python 01_data_cleaning.py

- Reads the three Excel files
- Standardizes empty / placeholder values
- Writes cleaned CSV files

### 7.3 Quality checks

    python 02_quality_checks.py

- Counts missing values in key columns
- Checks Cases + controls vs Total_Sample_Size consistency

### 7.4 Basic analysis

    python 03_basic_analysis.py

- Summarizes counts by Evidence_Tier, Subtype, Population, Effect_Measure

### 7.5 Visualization

    python 04_visualization.py

- Generates:
  - SNPs by Evidence Tier
  - Top subtypes (susceptibility)
  - Dataset size comparison

### 7.6 HTML database

    python 05_make_html.py

- Builds index.html with the full 52-SNP table
- Formats very small p-values in scientific notation

---

## 8. Outputs

- Cleaned CSVs for each dataset
- Quality-check summary (terminal)
- Basic statistical summary (terminal)
- Figures (snp_by_tier.png, snp_by_subtype.png, snp_by_dataset.png)
- Interactive-style HTML table (index.html)

---

## 9. Limitations

- Not every field was re-verified against the full text of every primary paper
- Some pharmacogenetic studies are small or report HR rather than OR
- Candidate SNPs may have mixed results across studies
- Population labels are taken from the primary reports and may be coarse

---

## 10. Suggested Next Improvements

- Mark selected high-confidence rows as VERIFIED after full paper re-check
- Add a simple search box to the HTML page
- Expand East Asian and other non-European coverage with equal annotation depth
- Optional: export a machine-readable JSON version of the curated table