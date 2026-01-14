# Repository Resume

This document provides a summary of the files contained in this repository, which track the evolution, performance, and strategic shifts of a predictive asset management program (2022-2025).

## 1. Annual Reports & Data (Source of Truth)
These files contain detailed tables of every successful predictive maintenance case, including asset names, failure modes, and financial value.
*   **`2022_Successful_Cases.md`**: 23 cases, Total Value: **$4.5M**. Dominance of Knowledge-Based models.
*   **`2023_Successful_Cases.md`**: 56 cases, Total Value: **$13.4M**. Peak volume of cases. High number of physical failures (rotating equipment).
*   **`2024_Successful_Cases.md`**: 46 cases, Total Value: **$14.1M**. Technological pivot to Machine Learning (74% of cases).
*   **`2025_Successful_Cases.md`** & **`2025_Report.md`**: 37 cases (detailed), Total Value: **$18.6M**. Introduction of high-value detection capabilities like Liquid Carry Over (LCO).

## 2. Analysis & Insights
High-level synthesis of the raw data, tracking trends in efficiency, technology, and financial impact.
*   **`Report_Analysis.md`**: Summarizes key metrics for each year (Total Alarms, Avoided Losses, Successful Cases).
    *   *Key Insight:* Total Value Avoided (2022-2025): **~$51.36 Million**.
*   **`2022-2025_Successful_Cases_Analysis.md`**: Detailed trend analysis.
    *   *Efficiency:* Value per case jumped from **$195k** (2022) to **~$501k** (2025).
    *   *Failure Modes:* Scaling and Physical Failures are the top value drivers.
*   **`Alarms_Pyramid_Analysis.md`**: Critical for understanding the "Noise" vs. "Signal" ratio.
    *   *Precision:* Improved from **49.1%** in 2024 (scaling pain) to **63.5%** in 2025 (AI impact).
    *   *Volume:* Total alarms dropped by **~49%** (2,754 to 1,407) in 2025 due to AI filtering.

## 3. Narrative Drafts (Phase 2 & 3)
Draft sections for the OTC Paper, describing the strategic "Phases" of the program.
*   **`phase2_draft.md` (2022-2024)**: "The Pivot to FMEA-based User Journeys." Focuses on moving from flat architecture to Asset-Centric Data Models and Knowledge-Based detection to solve scaling bottlenecks.
*   **`phase3_draft.md` (2025)**: "The Integration of LLMs and Risk-Based Prioritization." Focuses on using AI to solve the "Cognitive Bottleneck" (alert fatigue) and prioritizing maintenance based on risk.

## 4. Other Files
*   **`Paper_OTC.md`**: The master manuscript for the Offshore Technology Conference paper.
*   **`parse_table.py`**: Utility script for extracting data from report tables.
*   **`*.png`**: Visualizations (Charts) of the data.

---

## Strategic Summary for Draft Updates

**Data to Inject into Phase 2 (The Scaling Challenge):**
*   **Explosion of Alarms:** Mention the spike to **2,754 alarms** in 2024 as evidence of the scaling "noise" problem.
*   **Precision Dip:** Note the drop to **49.1% precision** in 2024.
*   **Value Growth:** Despite challenges, value grew from **$4.5M (2022)** to **$14.1M (2024)**.

**Data to Inject into Phase 3 (The AI Solution):**
*   **Noise Reduction:** AI implementation reduced total alarms by **~49%** (down to 1,407).
*   **Precision Peak:** Precision hit an all-time high of **63.5%**.
*   **High-Value Focus:** Average value per case reached **~$501k**, driven by complex detections like LCO ($1.7M+ value).
