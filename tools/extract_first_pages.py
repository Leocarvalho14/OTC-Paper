import sys
from pypdf import PdfReader, PdfWriter

def extract_pages(input_path, output_path, num_pages):
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        limit = min(num_pages, len(reader.pages))
        
        for i in range(limit):
            writer.add_page(reader.pages[i])
            
        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"Created {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <input> <output> <pages>")
        sys.exit(1)
        
    extract_pages(sys.argv[1], sys.argv[2], int(sys.argv[3]))
