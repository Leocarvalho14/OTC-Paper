import re

def parse_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find case starts: Type (ML/KB), No, Vessel, Date
    # Example: 11-12 ML 1.1 MV24 01/06/25
    # or: 59-60 KB 2025 3.1 MV27 11/12/24 (Wait, KB cases have year in No col sometimes? "KB 2025 3.1")
    # Let's look at page 9 content again.
    # "59-60 KB 2025\n3.1 MV27 11/12/24" -> It seems the formatting is a bit loose.
    
    cases = []
    
    # We will iterate through lines to find start of cases and end of cases
    lines = content.split('\n')
    current_case = {}
    collecting_desc = False
    
    # Pattern for ML cases: Page range? Type No Vessel Date
    # e.g. "11-12 ML 1.1 MV24 01/06/25"
    ml_pattern = re.compile(r'(?:ML|KB)\s+(?:2025\s+)?(\d+\.\d+)\s+(MV\d{2})\s+(\d{2}/\d{2}/\d{2})')
    
    for i, line in enumerate(lines):
        line = line.strip()
        match = ml_pattern.search(line)
        
        if match:
            # If we were processing a previous case, save it first
            if current_case:
                cases.append(current_case)
            
            current_case = {
                'id': match.group(1),
                'asset': match.group(2),
                'date': match.group(3),
                'description': [],
                'raw_end': [] # To capture the trailing numbers
            }
            # The description usually starts on the same line or next lines
            # Remove the matched prefix from the line to see if desc starts there
            # But the line often has junk before the match too (Page numbers)
            
            # Let's look for content after the date
            parts = line.split(match.group(3))
            if len(parts) > 1 and parts[1].strip():
                 current_case['description'].append(parts[1].strip())
            
            collecting_desc = True
            continue
        
        if collecting_desc:
            # Check if this line looks like the financial values line
            # It typically ends with numbers like "179.04 75,352 75,173"
            # Regex for the value line: (number or -) (number or -) (number)
            # e.g. "Sensor adjustment 179.04 75,352 75,173"
            
            # Simple check: does it end with 3 distinct number-like groups?
            # value pattern: [\d,]+\.?\d*
            val_pattern = re.compile(r'([\d,]+\.?\d*|-)\s+([\d,]+\.?\d*|-)\s+([\d,]+\.?\d*)$')
            val_match = val_pattern.search(line)
            
            if val_match:
                # Found the values
                y_val = val_match.group(2)
                current_case['y_val'] = y_val
                
                # The text before the values might be part of investigation results, not description
                # But for now, we assume description is everything before "Completed" or "Ongoing" or SAP numbers
                
                # Actually, Description is usually before "Completed"/"Ongoing"
                # Let's look for status keywords
                
                collecting_desc = False # Stop collecting for this case
            else:
                 # Check for Status keywords which denote end of description
                 if "Completed" in line or "Ongoing" in line:
                     # Description ends here usually
                     # But sometimes description is multi-line before this.
                     pass
                 
                 # Accumulate description if it's not a value line and not obviously something else
                 # This is heuristic.
                 if not line.startswith("Page"):
                     current_case['description'].append(line)

    # Append the last case
    if current_case:
        cases.append(current_case)

    # Post-processing
    final_cases = []
    for c in cases:
        # Filter description
        clean_desc = []
        status_found = False
        for d in c['description']:
            if "Completed" in d or "Ongoing" in d:
                status_found = True
                # The part before status might be desc
                pre_status = re.split(r'Completed|Ongoing', d)[0]
                if pre_status.strip():
                    clean_desc.append(pre_status.strip())
                break
            # Ignore SAP numbers if they appear in description lines
            if re.search(r'\d{8}', d): 
                continue
            clean_desc.append(d)
        
        full_desc = " ".join(clean_desc).strip()
        # Clean up some common artifacts
        full_desc = re.sub(r'^\d+\s+', '', full_desc) # Remove page nums if stuck
        
        # Only keep 2025 cases? The user said "2025 report... success cases".
        # The extraction includes cases with 2025 dates.
        # Check year in date
        if c['date'].endswith('25'):
            final_cases.append({
                'Case No': c['id'],
                'Title': full_desc,
                'Asset': c['asset'],
                'Value': c.get('y_val', 'N/A'),
                'Date': c['date']
            })

    return final_cases

cases = parse_report('2025_Report.md')

# Generate Markdown Table
print("| Case No | Title | Asset Involved | Intermediate Scenario Total Value (USD) | Date of the Case |")
print("| :---: | :--- | :---: | :---: | :---: |")
for c in cases:
    print(f"| {c['Case No']} | {c['Title']} | {c['Asset']} | ${c['Value']} | {c['Date']} |")
