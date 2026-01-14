def debug_file(file_path):
    print(f"--- Debugging {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        if "Machine" in line or "Knowledge" in line:
             if "2022" in line or "2023" in line:
                 print(f"CANDIDATE: {line.strip()}")

debug_file("2022 Report_Text.md")
debug_file("2023 Report_Text.md")
