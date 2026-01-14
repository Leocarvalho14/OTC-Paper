# Alarms Pyramid Analysis

Based on the analysis of the report resume PDF files, here is the pyramid analysis of alarms presenting the funnel from total alarms to closed cases.

| Year | Total Alarms | Useful Alarms | Precision (%) | Turned into Cases (Successful Cases) | Closed Cases |
|------|--------------|---------------|---------------|--------------------------------------|--------------|
| 2022 | N/A          | N/A           | N/A           | N/A                                  | N/A          |
| 2023 | 1,323        | 763           | 57.7%         | 55                                   | *Not specified in funnel* |
| 2024 | 2,754        | 1,353         | 49.1%         | 46                                   | 12           |
| 2025 | 1,407        | 893           | 63.5%         | 27                                   | *Not specified in funnel* |

**Notes:**
- **2022 Report:** The pyramid analysis graphic was not found in the provided resume file.
- **2023 Report:** The "Recommendations Funnel" presents 3 levels: Total Alarms, Total Useful Alarms, and Total Successful Cases. A distinct "Closed Cases" level was not present in the pyramid.
- **2024 Report:** The "Recommendations Funnel" explicitly presents 4 levels, distinguishing between "Total Successful Cases" (46) and "Total Closed Cases" (12).
- **2025 Report:** The "Recommendations Funnel" presents 3 levels similar to 2023. While supplementary charts mention "Completed Cases" (25), the funnel itself ends at "Total Successful Cases" (27).

---

## Critical Analysis: The Evolution of Signal-to-Noise

The evolution of the alarm funnel data strongly corroborates the strategic narrative outlined in the OTC Paper and Phase 2/3 drafts, illustrating a clear maturation from "detection" to "intelligent diagnosis."

### 1. The "Quality Jump" (Phase 2 Impact)
The transition from Phase 1 (unrecorded in this table, but referenced in drafts as having ~3-5% precision) to Phase 2 (2023) is marked by a high baseline precision of **57.7%**. This validates the strategic pivot to **FMEA-based user journeys** and **Knowledge-Based models**. By moving away from generic anomaly detection to specific failure-mode identification, the program established a strong foundation of trust, ensuring that more than half of all alerts generated were technically "useful" (true positives).

### 2. The Scaling Challenge (2024)
The data for 2024 reflects the classic "growing pains" of scaling. As the program expanded scope (likely to more vessels or asset classes), the **Total Alarms** spiked to **2,754**—double the previous year. Correspondingly, the **Precision** dipped to **49.1%**. This increase in volume and noise likely contributed to the "alert fatigue" described in the Phase 3 draft, where the sheer quantity of signals—even if half were useful—began to overwhelm the engineering teams, creating a cognitive bottleneck.

### 3. The "AI Dividend" (Phase 3 Impact)
The 2025 data clearly demonstrates the impact of the **Phase 3 interventions**, specifically the integration of the **Cognitive Diagnostic Module (LLMs)** and **Risk-Based Prioritization**.
*   **Noise Reduction:** Total alarms dropped drastically to **1,407** (a ~49% reduction from 2024), bringing the volume back to manageable levels.
*   **Precision Peak:** Despite the volume drop, the quality of alerts reached an all-time high of **63.5%**.
This confirms that the AI integration successfully filtered out non-actionable "noise" and operational transients that traditional models (even FMEA-based ones) might catch, acting as an effective first-line analyst.

### 4. The "Useful" vs. "Successful" Gap
A persistent trend is the significant gap between **Useful Alarms** (hundreds/thousands) and **Successful Cases** (dozens). This indicates that while the system is excellent at detecting technical anomalies (e.g., "Vibration is high"), only a small fraction (~3-7%) warrant a "Success Case" designation (action taken + value generated). This disparity highlights the necessity of the **Risk-Based Prioritization** introduced in Phase 3. The system has matured from simply asking "Is it broken?" (Detection) to "Does it matter right now?" (Risk Management), ensuring that engineering effort is focused solely on the high-value cases that drive the $13.6M savings, rather than chasing every minor deviation.
