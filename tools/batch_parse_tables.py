import re
import sys

def parse_and_save(year):
    input_file = f"{year} Report_Text.md"
    output_file = f"{year}_Successful_Cases.md"
    
    print(f"Processing {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cases = []
    lines = content.split('\n')
    current_case = {}
    collecting_desc = False
    
    # Updated Regex to be more flexible with years and formats
    # Matches: "ML 1.1 MV24 01/06/25" OR "1.1 MV24 01/06/2024" etc.
    # Also sometimes headers have "ML 2024" or just "1.1"
    # Let's try a pattern that looks for Case No + MVxx + Date
    # Case No: \d+\.\d+
    # Asset: MV\d{2}
    # Date: \d{1,2}/\d{1,2}/\d{2,4}
    
    case_pattern = re.compile(r'(?:ML|KB)?\s*(?:20\d{2})?\s*(\d+\.\d+)\s+(MV\d{2})\s+(\d{1,2}/\d{1,2}/\d{2,4})')
    
    # Value Pattern: Cost | Saving | Net
    # Finds lines ending with 3 numbers/dashes
    val_pattern = re.compile(r'([\d,]+\.?\d*|-)\s+([\d,]+\.?\d*|-)\s+([\d,]+\.?\d*)$')

    for line in lines:
        line = line.strip()
        match = case_pattern.search(line)
        
        if match:
            if current_case:
                cases.append(current_case)
            
            current_case = {
                'id': match.group(1),
                'asset': match.group(2),
                'date': match.group(3),
                'description': [],
                'value': 'N/A'
            }
            
            # Capture description from the same line
            parts = line.split(match.group(3))
            if len(parts) > 1 and parts[1].strip():
                 current_case['description'].append(parts[1].strip())
            
            collecting_desc = True
            continue
        
        if collecting_desc:
            val_match = val_pattern.search(line)
            if val_match:
                # Group 2 is usually the intermediate value
                current_case['value'] = val_match.group(2)
                collecting_desc = False
            else:
                # Stop conditions
                if "Completed" in line or "Ongoing" in line or line.startswith("## Page") or "Investigation Results" in line:
                    pass
                elif "SAP Note" in line or "WO" in line:
                    pass
                else:
                     if not re.match(r'^\d+$', line): # Skip page numbers
                        current_case['description'].append(line)

    if current_case:
        cases.append(current_case)

    # Write to Markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {year} Successful Cases\n\n")
        f.write("| Case No | Title | Asset Involved | Intermediate Scenario Value (USD) | Date |\n")
        f.write("| :---: | :--- | :---: | :---: | :---: |\n")
        
        total_sum = 0.0
        
        for c in cases:
            full_desc = " ".join(c['description']).strip()
            # Clean common garbage
            full_desc = re.sub(r'^\d+\s+', '', full_desc)
            full_desc = full_desc.replace('Machine Learning', '').replace('Knowledge Based', '').strip()
            
            # Value Calculation
            val_str = c['value']
            try:
                clean_val = val_str.replace(',', '').replace('-', '0').replace('$', '')
                if clean_val.strip() == '': clean_val = '0'
                total_sum += float(clean_val)
            except:
                pass
                
            display_val = f"${val_str}" if val_str not in ['-', 'N/A'] else "N/A"
            
            f.write(f"| {c['id']} | {full_desc} | {c['asset']} | {display_val} | {c['date']} |\n")
            
        f.write(f"| **TOTAL** | | | **${total_sum:,.0f}** | |\n")
    
    print(f"Generated {output_file} with {len(cases)} cases.")

# Run for all years
for y in [2022, 2023, 2024]:
    parse_and_save(y)
