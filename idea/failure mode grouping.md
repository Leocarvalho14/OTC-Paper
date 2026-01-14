# Failure Mode Grouping Rules

These rules categorize predictive maintenance cases based on specific keywords found in the **Case Title**. The categorization is applied in the following order of priority:

## 1. Abnormal Instrument Reading
*   **Keywords:** `"abnormal instrument"`
*   **Description:** Cases related to sensor faults, reading discrepancies, or instrument malfunctions.

## 2. Scaling
*   **Keywords:** `"scaling"`
*   **Description:** Cases involving the accumulation of scale deposits in heat exchangers or other process equipment.

## 3. LCO (Liquid Carry Over)
*   **Keywords:** `"lco"` OR `"liquid carry over"`
*   **Description:** Cases related to liquid ingestion in compressors or scrubbers.

## 4. Physical Failures (Rotating Equipments)
*   **Keywords:** (None - Default Category)
*   **Description:** Any case that does **not** match the above categories. This typically includes mechanical issues such as:
    *   High vibration
    *   Lube oil leakage / pressure issues
    *   High temperatures (bearings, stators) not flagged as "instrument reading"
    *   Seal gas issues
    *   Surge/Stall events
