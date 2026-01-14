# Phase 2: The Pivot to FMEA-based User Journeys (2022-2024)

Following the validation of the Proof of Concept in Phase 1, the program faced specific challenges related to scalability. The objective was to expand the scope from a pilot set of assets to fleet-wide monitoring. However, a critical structural flaw was identified: the linear relationship between engineering effort and asset count created an unsustainable bottleneck. To overcome this, the team formulated three core hypotheses to guide the program's expansion:

**Hypotheses**
*   **Hypothesis 1 (Relevance & Precision):** Implementing logic derived from Failure Mode, Effects, and Criticality Analysis (FMECA) will improve alarm precision by filtering operational noise and strictly defining "useful alarms" based on engineering context.
*   **Hypothesis 2 (Scalability via Abstraction):** An **Asset-Centric Data Model** (Semantic Layer) is required to decouple analytical logic from raw historian tags. This abstraction is necessary to enable a "Write Once, Deploy Many" architecture, breaking the linear dependency between development effort and asset count.
*   **Hypothesis 3 (Diagnostic Efficiency):** Centralizing all operational context—sensors, active alarms, and documentation—into a unified web interface will significantly reduce the Mean Time to Diagnosis (MTTD).

**FMECA Integration and Knowledge-Based Models (Addressing Hypothesis 1)**
To validate Hypothesis 1, the team conducted extensive workshops with subject matter experts to redefine the criteria for "useful alarms." Using the ISO 13379 series as a framework, the program pivoted from generic anomaly detection to specific failure mode identification.

This shift led to the widespread adoption of **Knowledge-Based models**, which utilize engineering equations and pre-established design limits to identify known failure patterns. Unlike generic data-driven alerts, these models direct the user's attention to specific, actionable issues (e.g., distinguishing "Lube Oil Filter Clogging" from general "Vibration Anomaly"). This approach drastically reduced false positives and standardized the definition of a "success case" from simply "catching an anomaly" to "preventing a specific failure mode." The impact of this "Quality Jump" was profound: while Phase 1 models operated with an estimated precision of 3-5%, the transition to FMEA-based logic raised the baseline precision to **57.7% in 2023**, ensuring that the majority of alerts generated were technically valid. By 2023, these Knowledge-Based models were the primary engine of the program, accounting for **70% of all successful cases**.

**The Asset-Centric Data Model (Addressing Hypothesis 2)**
Hypothesis 2 addressed the primary technical bottleneck: the Phase 1 "Direct Tag Binding" architecture. In that initial flat architecture, analytical models were coupled directly to raw sensor tags (e.g., `40_TI_1434.PV`) within the historian database. This created significant friction:
*   **Manual Mapping:** Deploying a model to a new asset required manually locating and hard-coding specific tags, as nomenclature varied significantly between FPSOs.
*   **Fragility:** If a sensor was replaced and its tag name changed, the hard-coded link would break, causing model failure.
*   **Developer Waste:** Developers spent an estimated 80% of their time on tag mapping rather than analytical development.

To resolve this, the team implemented the **Asset-Centric Data Model**, a semantic abstraction layer that functions through a two-step process:
1.  **Normalization:** Raw historian identifiers are mapped once to a standardized "Asset Template." For example, tag `40_TI_1434.PV` is mapped to the standard attribute `Radial Bearing Temp. DE` (Drive End) within the Compressor class.
2.  **Abstraction:** Analytical models are re-written to ingest these standard attributes.

This semantic layer fundamentally changed deployment velocity. By decoupling model logic from the data source, the program achieved a **"Write Once, Deploy Many"** capability. A model defined for a specific equipment class (e.g., Water Injection Pumps) could be instantly instantiated across hundreds of identical assets. This architecture shifted engineering focus from data wrangling to value-added tasks such as model tuning and failure analysis.

**Standardization and Diagnostic Efficiency (Addressing Hypothesis 3)**
Addressing Hypothesis 3, the new application interface leveraged the contextualized data layer to streamline the diagnosis workflow. By aggregating all digital information—real-time sensor trends, historical alarms, and technical documentation—into a single view, the interface eliminated the need for engineers to cross-reference multiple systems.

Metrics tracking user behavior confirmed that this centralization significantly reduced the cognitive load during investigations. By the end of Phase 2, the program had achieved significant milestones:

*   **Value Generation:** Annual avoided losses grew significantly, from **$4.5 million in 2022** to **$14.1 million in 2024**.
*   **Efficiency:** The average value per successful case increased from **$195k** to **$307k**, indicating a shift towards capturing more critical failures.
*   **The Cost of Scale:** However, scaling also brought challenges. As the asset count grew, so did the noise. In 2024, the total alarm count spiked to **2,754** with a precision of **49.1%**, creating an unsustainable workload for the engineering team.

These strategic pivots in Phase 2 successfully solved the *data* scalability problem, but the resulting flood of alerts highlighted the need for the advanced *cognitive* integration that would define Phase 3.