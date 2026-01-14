# Phase 2: The Pivot to FMEA-based User Journeys (2022-2024)

Following the validation of the Proof of Concept in Phase 1, the program faced specific challenges related to scalability. The objective was to expand the scope from XXX assets and XX sensors to YYY assets and XXX sensors. However, a critical structural flaw was identified: the linear relationship between engineering effort and asset count created an unsustainable bottleneck. To overcome this, the team formulated three core hypotheses to guide the program's expansion:

**Hypotheses**
*   **Hypothesis 1 (Contextualization of assets data / Failure Mode Analysis):** In order to address the major problem identified in phase one related to “low precision” (quantity of false alarms), it was observed by the user interviews that the proper definition of what should be a useful alarm was missing. What if we apply a Failure Mode and Causes Analysis (FMECA) methodology with subject matter experts to better understand possible detection scenarios already known by engineers?
*   **Hypothesis 2 (Asset-Centric Data Model):** While Hypothesis 1 addressed the quality of the alerts, Hypothesis 2 addressed the scalability of the deployment. As the program prepared to expand from a pilot scope to fleet-wide monitoring, structural bottlenecks in the data architecture became apparent. What if all data consumed by the models comes from a data organization layer that contextualizes data, decoupling the analytical logic from the raw database?
*   **Hypothesis 3 (Integrated User Interface):** Introduce a web application to allow user to interact with data and use context information for diagnosis, centralizing all digital information related to the asset (sensors, alarms, documentation) in a single place to expedite the diagnosis phase.

**FMECA Integration and Knowledge-Based Models (Addressing Hypothesis 1)**
To validate Hypothesis 1, workshops were conducted with subject matter experts to capture their knowledge and expertise on what kind of issues should be alarming and what information the alarm should contain to expedite their diagnosis phase. This methodology was strongly inspired in ISO 13379 series.
This shift led to the adoption of "Knowledge-Based" models, which utilize engineering equations and pre-established design limits based on asset project design to raise alerts. Unlike generic alerts, these models directed the user's attention to specific, actionable issues. This approach drastically reduced diagnosis time and standardized the definition of a "success case" from "catching an anomaly" to "preventing a failure mode."

**The Asset-Centric Data Model (Addressing Hypothesis 2)**
While Hypothesis 1 addressed the quality of the alerts, Hypothesis 2 addressed the scalability of the deployment. As the program prepared to expand from a pilot scope to fleet-wide monitoring, structural bottlenecks in the data architecture became apparent.
In Phase 1, the system utilized a "flat" architecture characterized by Direct Tag Binding. Analytical models were connected directly to raw sensor tags (e.g., 40_TI_1434.PV) within the historian database. This approach presented significant friction during expansion:
*   Developing a model for "Compressor A" required a data scientist to manually locate specific tags and hard-code them into the algorithm.
*   Deploying the same model to "Compressor B" was not a simple replication. Because tag nomenclature often varies between assets (and even more so between different FPSOs), engineers had to manually map new tags (e.g., 40_TI_1433.PV) for every new instance.
*   If a sensor was replaced and the tag name changed in the PIMS, the hard-coded link would break, causing model failure.

This linear relationship between engineering effort and asset count meant that scaling to thousands of assets would require an unsustainable amount of manual configuration. To resolve this, the team implemented an **Asset-Centric Data Model**, introducing an abstraction layer between the raw data and the models. This semantic layer functions through a two-step process:
1.  Raw, cryptic tags are mapped once to a standardized "Asset Template." For example, tag 40_TI_1434.PV is mapped to the standard attribute "Radial Bearing Temp. DE" (Drive End) within the Compressor class.
2.  The analytical models are re-written to ingest the standard attribute ("Radial Bearing Temp") rather than a specific tag number.

The implementation of the semantic layer fundamentally changed the deployment velocity. By decoupling the model logic from the data source, the program achieved:
*   **Models became "write once, deploy many."** Once a model is defined for a class of equipment (e.g., Water Injection Pumps), it can be instantly instantiated across all assets that share that template, as the data mapping is handled upstream.
*   **Resilience:** Changes to raw tags are managed in the semantic layer, leaving the model logic untouched and robust.
*   **Focus Shift:** This architecture shifted the developer focus. Prior to this layer, developers spent an estimated 80% of their time searching for and mapping tags. With the semantic layer, this time is reallocated to value-added tasks such as failure mode analysis and model tuning.

**Standardization and Diagnostic Efficiency (Addressing Hypothesis 3)**
The new application interface leveraged the context data layer to play a significant role in expediting the diagnosis step. By compiling all digital information related to the asset in a single place, users could easily check asset sensors not explicitly used by the alarming model and compare alarms from other failure modes for the same asset simultaneously.
It was also possible to start tracking user behavior on the application and turn it to metrics that support the Design Thinking for Innovation (DTI) process workflow, understanding which information is mostly used by users in the diagnosis phase. These pivots allowed the program to scale from monitoring hundreds to thousands of assets while simultaneously increasing alarm precision.
