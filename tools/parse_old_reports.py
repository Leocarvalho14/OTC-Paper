import re

def parse_2022(file_path):
    print(f"Parsing 2022 from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    cases = []
    # Pattern: ID (Start) $Value Description Approach Date ...
    # Regex: ^(\d+)\s+(\$[\d,.]+)\s+(.*?)\s+(Machine learning|Knowledge-based)\s+(\d{4}-\d{2}-\d{2})
    # We ignore the end of the line as it's messy
    pattern = re.compile(r'^(\d+)\s+(\$[\d,.]+)\s+(.*?)\s+(Machine learning|Knowledge-based)\s+(\d{4}-\d{2}-\d{2})', re.IGNORECASE)
    
    for line in lines:
        line = line.strip()
        match = pattern.search(line)
        if match:
            # Asset is tricky, usually at the end. Let's try to find MVxx in the whole line
            asset_match = re.search(r'(MV\d{2})', line)
            asset = asset_match.group(1) if asset_match else "Unknown"
            
            val_clean = match.group(2).replace('$', '').replace('.', '') # 500.000 -> 500000
            
            cases.append({
                'id': match.group(1),
                'value': val_clean,
                'desc': match.group(3),
                'date': match.group(5),
                'asset': asset
            })
            
    return cases

def parse_2023(file_path):
    print(f"Parsing 2023 from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    cases = []
    # Pattern: Value(merged?)Description Approach Date ... ID
    # Regex to split Value from Description (Value ends with digit, Desc starts with Letter)
    # 211,024Gas -> 211,024 and Gas
    
    # We look for lines containing "Machine Learning" or "Knowledge-based" and a Date
    base_pattern = re.compile(r'(Machine Learning|Knowledge[- ]based)\s+(\d{4}-\d{2}-\d{2})', re.IGNORECASE)
    
    for line in lines:
        line = line.strip()
        # Filter lines that look like table rows
        if not base_pattern.search(line): continue
        
        # Try to extract Value at start
        # Matches numbers, commas, optionally $ at start.
        # Strict start: ^(\$?[0-9,]+)(.*)$
        val_match = re.match(r'^(\$?[0-9,]+)(.*)$', line)
        
        if val_match:
            raw_val = val_match.group(1)
            rest_line = val_match.group(2)
            
            # Extract Case ID at the end (e.g., "1.1")
            # But sometimes it's merged "MV241.1"
            id_match = re.search(r'(\d+\.\d+)$', rest_line)
            case_id = id_match.group(1) if id_match else "N/A"
            if case_id == "N/A":
                # Maybe merged at end: "MV241.1" -> ID 1.1? No, usually distinct.
                # Let's check debug output: "MV241.1"
                # Regex for "at least one char then digits.digits": (?<=\D)(\d+\.\d+)$ 
                id_match = re.search(r'(?<=\D)(\d+\.\d+)$', rest_line)
                case_id = id_match.group(1) if id_match else "N/A"

            # Asset
            asset_match = re.search(r'(MV\d{2})', rest_line)
            asset = asset_match.group(1) if asset_match else "Unknown"
            
            # Date and Approach
            mid_match = base_pattern.search(rest_line)
            date = mid_match.group(2) if mid_match else "Unknown"
            
            # Description is text between Value and Approach
            # Raw: "Gas Turbine...Machine Learning"
            # Split rest_line by Approach
            if mid_match:
                desc_part = rest_line.split(mid_match.group(1))[0].strip()
                desc = desc_part
            else:
                desc = "Description parse failed"

            val_clean = raw_val.replace('$', '').replace(',', '')
            
            cases.append({
                'id': case_id,
                'value': val_clean,
                'desc': desc,
                'date': date,
                'asset': asset
            })
            
    return cases

def save_markdown(cases, year):
    output_file = f"{year}_Successful_Cases.md"
    total = 0.0
    
    # Sort by ID if possible
    try:
        cases.sort(key=lambda x: float(x['id']) if x['id'] != 'N/A' else 999)
    except:
        pass

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {year} Successful Cases\n\n")
        f.write("| Case No | Title | Asset Involved | Intermediate Scenario Value (USD) | Date |\n")
        f.write("| :---: | :--- | :---: | :---: | :---: |\n")
        
        for c in cases:
            try:
                clean_val_float = float(c['value'])
                total += clean_val_float
                display_val = f"${clean_val_float:,.0f}"
            except:
                display_val = f"${c['value']}"

            f.write(f"| {c['id']} | {c['desc']} | {c['asset']} | {display_val} | {c['date']} |\n")
            
        f.write(f"| **TOTAL** | | | **${total:,.0f}** | |\n")
    print(f"Saved {output_file} with {len(cases)} cases")

# EXECUTION
try:
    cases_2022 = parse_2022("2022 Report_Text.md")
    save_markdown(cases_2022, 2022)

    cases_2023 = parse_2023("2023 Report_Text.md")
    save_markdown(cases_2023, 2023)
except Exception as e:
    print(f"An error occurred: {e}")
