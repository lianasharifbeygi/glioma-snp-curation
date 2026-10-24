# Curation and Population-Aware Annotation of Glioma-Associated SNPs

## Project Overview
This project curates and annotates SNPs associated with glioma risk, treatment response, and prognosis.
It started as a course assignment and was developed into a structured mini bioinformatics project.

## Dataset Summary
- Total SNPs: 52
- Susceptibility SNPs: 40 (Tier1 + Tier3)
- Pharmacogenetic SNPs: 8 (Tier2)
- Needs evidence review: 4

## Data Structure
- `data/cleaned_susceptibility.csv`
- `data/cleaned_pharmacogenetics.csv`
- `data/cleaned_needs_review.csv`

## Analysis Scripts
- `01_data_cleaning.py` — clean and standardize raw tables
- `02_quality_checks.py` — missing values and sample-size consistency
- `03_basic_analysis.py` — summary statistics
- `04_visualization.py` — generate figures

## Figures
- Number of SNPs by Evidence Tier
- Top subtypes in susceptibility SNPs
- Dataset size comparison

## Notes
- All sequences (FASTA) are standardized to 101 bp (SNP at position 51).
- Citation counts were extracted from a single source on 2026-10-10.
- QC status is mostly PARTIAL (not fully verified against every primary paper).

## Limitations
- Some pharmacogenetic studies report HR instead of OR.
- A few candidate SNPs have mixed or weak evidence.
- Sample sizes for subtype-specific analyses differ from the full study total.

## Author
Undergraduate Biotechnology student project (course internship / mini-project).