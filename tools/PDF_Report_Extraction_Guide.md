# PDF Report Extraction Workflow

This guide documents the procedure and tools used to extract structured "Successful Cases" tables from annual operational reports (PDF format). It is designed to be reusable for future reports.

## Objective
Convert a PDF report containing narrative descriptions of industrial cases into a structured Markdown table with the following columns:
*   Case Number
*   Title/Description
*   Asset Involved
*   Value (USD)
*   Date

## Prerequisites
*   **Python 3.x**
*   **Package Manager:** `uv` (recommended) or `pip`
*   **Libraries:** `pypdf`

---

## Step 1: Convert PDF to Text
First, we extract the raw text from the PDF to make it parseable. This script ignores images and layout, focusing on the content.

**Script:** `pdf_to_text.py`

```python
from pypdf import PdfReader
import sys

# CONFIGURATION
INPUT_PDF = "Target_Report.pdf"  # CHANGE THIS to your new filename
OUTPUT_MD = "Report_Text.md"

try:
    reader = PdfReader(INPUT_PDF)
    text_content = []
    
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            text_content.append(f"## Page {i+1}\n\n{text}\n")
    
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(f"# {INPUT_PDF} (Text Extraction)\n\n")
        f.write("\n".join(text_content))
        
    print(f"Successfully converted {INPUT_PDF} to {OUTPUT_MD}")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
```

**Usage:**
```bash
uv run --with pypdf python3 pdf_to_text.py
```

---

## Step 2: Parse Text to Table
This script uses Regular Expressions (Regex) to identify case patterns (e.g., "1.1 MV24 01/06/25") and extract associated financial data.

**Script:** `parse_table.py`

```python
import re
import sys

# CONFIGURATION
INPUT_TEXT_FILE = "Report_Text.md" # The output from Step 1

def parse_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cases = []
    lines = content.split('\n')
    current_case = {}
    collecting_desc = False
    
    # REGEX PATTERN: Matches "Type No Asset Date" (e.g., "ML 1.1 MV24 01/06/25")
    # Adjust '2025' to the relevant year if hardcoded in report headers
    case_pattern = re.compile(r'(?:ML|KB)\s+(?:20\d{2}\s+)?(\d+\.\d+)\s+(MV\d{2})\s+(\d{2}/\d{2}/\d{2})')
    
    # REGEX PATTERN: Matches financial lines (e.g., "179.04 75,352 75,173")
    val_pattern = re.compile(r'([\d,]+\.?\d*|-)\s+([\d,]+\.?\d*|-)\s+([\d,]+\.?\d*)$')

    for line in lines:
        line = line.strip()
        match = case_pattern.search(line)
        
        if match:
            # Save previous case
            if current_case:
                cases.append(current_case)
            
            # Start new case
            current_case = {
                'id': match.group(1),
                'asset': match.group(2),
                'date': match.group(3),
                'description': [],
                'value': 'N/A'
            }
            
            # Capture description immediately following date if present
            parts = line.split(match.group(3))
            if len(parts) > 1 and parts[1].strip():
                 current_case['description'].append(parts[1].strip())
            
            collecting_desc = True
            continue
        
        if collecting_desc:
            # Check if this is the value line
            val_match = val_pattern.search(line)
            if val_match:
                # The middle column is usually the Intermediate/Actual Saving
                # Value structure often: Cost | Saving | Net
                current_case['value'] = val_match.group(2) 
                collecting_desc = False # Done with this case
            else:
                # Stop if we hit status keywords or new page headers
                if "Completed" in line or "Ongoing" in line or line.startswith("## Page"):
                    pass # Don't add these to description
                else:
                    # Clean up common artifacts (like trailing page numbers)
                    if not re.match(r'^\d+$', line):
                        current_case['description'].append(line)

    # Append last case
    if current_case:
        cases.append(current_case)

    return cases

def format_value(val_str):
    if val_str in ['-', 'N/A']: return "N/A"
    return f"${val_str}"

# Execution
cases = parse_report(INPUT_TEXT_FILE)

print("| Case No | Title | Asset Involved | Intermediate Scenario Value (USD) | Date |")
print("| :---: | :--- | :---: | :---: | :---: |")

total_sum = 0.0

for c in cases:
    # Clean Description
    full_desc = " ".join(c['description']).strip()
    full_desc = re.sub(r'^\d+\s+', '', full_desc) # Remove leading numbers
    
    # Calculate Total
    try:
        clean_val = c['value'].replace(',', '').replace('-', '0')
        total_sum += float(clean_val)
    except:
        pass

    print(f"| {c['id']} | {full_desc} | {c['asset']} | {format_value(c['value'])} | {c['date']} |")

print(f"| **TOTAL** | | | **${total_sum:,.0f}** | |")
```

**Usage:**
```bash
python3 parse_table.py > Successful_Cases_Table.md
```

## Step 3: Manual Verification
After generating the table:
1.  Check for rows with `N/A` or `$0` values. This usually indicates the text extraction formatting was irregular (e.g., missing columns or merged lines).
2.  Open the `Report_Text.md` file, search for the specific Case ID, and manually locate the correct value.
3.  Update the final Markdown table manually.
