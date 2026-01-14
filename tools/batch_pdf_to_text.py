from pypdf import PdfReader
import sys

reports = [
    "2022 Report.pdf",
    "2023 Report.pdf",
    "2024 Report.pdf"
]

for report in reports:
    try:
        output_md = report.replace(".pdf", "_Text.md")
        reader = PdfReader(report)
        text_content = []
        
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                text_content.append(f"## Page {i+1}\n\n{text}\n")
        
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(f"# {report} (Text Extraction)\n\n")
            f.write("\n".join(text_content))
            
        print(f"Successfully converted {report} to {output_md}")
    except Exception as e:
        print(f"Error processing {report}: {e}")
