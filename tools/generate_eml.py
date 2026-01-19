import sys
import re
from email.message import EmailMessage

def format_text(text):
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    return text

def markdown_to_html(text):
    html_lines = []
    in_table = False
    table_lines = []
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        
        # Table handling
        if line.startswith('|'):
            in_table = True
            table_lines.append(line)
            continue
        else:
            if in_table:
                # Process the accumulated table
                html_lines.append(process_table(table_lines))
                table_lines = []
                in_table = False
            
            if not line:
                html_lines.append('<br>')
                continue
                
            # Headers
            if line.startswith('## '):
                html_lines.append(f'<h2>{format_text(line[3:])}</h2>')
            elif line.startswith('# '):
                html_lines.append(f'<h1>{format_text(line[2:])}</h1>')
            elif line.startswith('---'):
                html_lines.append('<hr>')
            else:
                # Text formatting
                html_lines.append(f'<p>{format_text(line)}</p>')
                
    if in_table:
        html_lines.append(process_table(table_lines))
        
    return '\n'.join(html_lines)

def process_table(lines):
    html = '<table border="1" style="border-collapse: collapse; width: 100%; margin-top: 10px; margin-bottom: 10px;">'
    
    # Header
    header = lines[0]
    headers = [c.strip() for c in header.strip('|').split('|')]
    html += '<thead><tr>'
    for h in headers:
        html += f'<th style="padding: 8px; background-color: #f2f2f2; border: 1px solid #ddd;">{format_text(h)}</th>'
    html += '</tr></thead><tbody>'
    
    # Skip separator line (usually 2nd line)
    start_idx = 1
    if len(lines) > 1 and '---' in lines[1]:
        start_idx = 2
        
    for line in lines[start_idx:]:
        cells = [c.strip() for c in line.strip('|').split('|')]
        html += '<tr>'
        for c in cells:
            html += f'<td style="padding: 8px; border: 1px solid #ddd;">{format_text(c)}</td>'
        html += '</tr>'
        
    html += '</tbody></table>'
    return html

def main():
    input_filename = '2025 q4 cases by vessel.md'
    output_filename = '2025_Q4_Cases_Report.eml'
    
    try:
        with open(input_filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")
        sys.exit(1)

    # Extract Subject
    subject_match = re.search(r'\*\*Subject:\*\*\s*(.*)', content)
    subject = subject_match.group(1).strip() if subject_match else "Q4 2025 Successful Cases Overview"

    # Prepare Body
    # Remove the metadata lines at the top for the email body to avoid redundancy
    # We look for "Dear Managers" to start the body, or just strip the first few lines if we know format.
    # The file has:
    # # Email Draft...
    # **Subject:** ...
    # 
    # Dear Managers...
    
    # Let's start body from "Dear Managers" if present, otherwise just strip first 3 lines.
    start_pattern = "Dear Managers,"
    idx = content.find(start_pattern)
    if idx != -1:
        body_content = content[idx:]
    else:
        # Fallback: simple strip of header
        body_content = re.sub(r'^# Email Draft:.*\n+', '', content)
        body_content = re.sub(r'\*\*Subject:\*\*.*\n+', '', body_content)
    
    html_content = markdown_to_html(body_content)

    html_body = f"""
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
    </style>
    </head>
    <body>
    {html_content}
    </body>
    </html>
    """

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "Predictive Maintenance Team <pred.maint@example.com>"
    msg['To'] = "Managers <managers@example.com>"
    msg.set_content("This email contains HTML content. Please enable HTML viewing.")
    msg.add_alternative(html_body, subtype='html')

    with open(output_filename, 'wb') as f:
        f.write(msg.as_bytes())
    
    print(f"Successfully generated {output_filename}")

if __name__ == "__main__":
    main()
