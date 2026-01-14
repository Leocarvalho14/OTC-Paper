# Guidelines for Case Data Digestion from PDF Reports

This document outlines the standard procedure for extracting, cleaning, and summarizing successful case data from extracted report text files.

## 1. Data Extraction Workflow

### Identify Source Files
*   Locate the text-extracted version of the annual report (e.g., `2024 Report_Text.md`).
*   Verify the report period to ensure you are analyzing the correct year.

### Locate Relevant Sections
*   **Summary Tables**: Look for pages titled "Summary of successful cases" or "Successful cases status". These usually provide a high-level list of case numbers, vessels, dates, and values.
*   **Detailed Case Pages**: Find individual pages titled "CASE X.Y". These provide the most accurate "Intermediate Scenario Value", detailed descriptions, and specific page references.

### Required Data Points
For each case, extract:
1.  **Case No**: The identifier (e.g., 1.1, 2.3).
2.  **Title**: Concise description of the event.
3.  **Asset Involved**: The vessel or equipment ID (e.g., MV24, MV30).
4.  **Value (USD)**: Standardize on the **Intermediate Scenario Value** unless otherwise specified.
5.  **Date**: The event or notification date.
6.  **Page Reference**: The physical page number in the PDF where the case detail is located.
7.  **Failure Mode**: Categorize based on the case description (e.g., Scaling, Abnormal Instrument Reading, Physical Failures).

## 2. Categorization Logic

Categorize cases by their identification number prefixes:
*   **1.x**: Machine Learning Cases.
*   **2.x**: Scaling Cases.
*   **3.x**: Knowledge Based Cases.

*Note: Special failure modes like "LCO (Liquid Carry Over)" should be explicitly called out in consolidated tables if they appear in the report.*

## 3. Summarization Tables

Every digested report should include three distinct sections:
1.  **Successful Cases Detail**: A full list of all extracted cases with their specific values and references.
2.  **Consolidated by Failure Mode**: A summary table totaling quantities and values grouped by the nature of the failure (e.g., Scaling, Physical Failures).
3.  **Cases per Type**: A summary table totaling quantities and values based on the identification prefix (ML, Scaling, Knowledge Based).

## 4. Common Pitfalls to Avoid

*   **Markdown Table Formatting**: Ensure the separator line (e.g., `| :---: | :--- |`) has exactly the same number of columns as the header. A mismatch will break the table rendering.
*   **Overlapping Years**: Reports often include "Ongoing" cases from the previous year. Verify whether the task requires strictly "newly opened" cases or all "currently active" cases.
*   **Scenario Confusion**: Be careful not to mix "Best Scenario" or "Worst Scenario" values with the "Intermediate" ones. Always verify which column you are reading from the assessment box.
*   **File Truncation**: PDF extraction text can be extremely long. Ensure you have read the entire file (using offsets) before assuming a case is missing.
*   **Decimal vs. Integer Values**: Some reports use commas for decimals and others for thousands (e.g., $1.000 vs $1,000). Always confirm the numerical scale before totaling.
*   **Asset Consistency**: Standardize vessel names (e.g., "MV 24" vs "MV24") to ensure summary counts are accurate.

## 5. Example Output (Digested 2024 Data)

### Successful Cases Detail
| Case No | Title | Asset Involved | Intermediate Scenario Value (USD) | Date | Page | 
| :---: | :--- | :---: | :---: | :---: | :---: | 
| 1.1 | Compressor bearing vibration increase (RE-INJECTION) | MV26 | $361,911 | 12/09/23 | 14 | 
| 2.1 | Scaling signs on Crude Heater A | MV32 | $1,114,719 | 01/17/24 | 50 | 
| 3.1 | Low liquid fuel pressure | MV26 | $125,375 | 01/04/24 | 53 | 
| ... | ... | ... | ... | ... | ... | 
| **TOTAL** | | | **$14,139,761** | | |

### Consolidated by Failure Mode
| Failure Mode | Quantity | Total Value (USD) |
| :--- | :---: | :---: | 
| Physical Failures (Rotating Equipments) | 15 | $4,217,324 |
| Abnormal Instrument Reading | 28 | $5,898,284 |
| LCO (Liquid Carry Over) | 1 | $912,416 |
| Scaling | 2 | $3,111,737 |
| **TOTAL** | **46** | **$14,139,761** |

### Cases per Type
| Type | Quantity | Total Value (USD) |
| :--- | :---: | :---: | 
| Machine Learning Cases | 34 | $7,257,167 |
| Scaling Cases | 2 | $3,111,737 |
| Knowledge Based Cases | 10 | $3,770,857 |
| **TOTAL** | **46** | **$14,139,761** |
