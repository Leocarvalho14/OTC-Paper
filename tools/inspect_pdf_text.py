from pypdf import PdfReader
import sys

def inspect_text(file_path):
    try:
        reader = PdfReader(file_path)
        for i in range(min(6, len(reader.pages))):
            print(f"--- Page {i+1} ---")
            print(reader.pages[i].extract_text())
            print("\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_text(sys.argv[1])

