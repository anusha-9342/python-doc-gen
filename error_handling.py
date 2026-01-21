import sys
import pandas as pd
from docx import Document

try:
    doc = Document("template.docx")
except FileNotFoundError:
    print("Error: template.docx not found")
    sys.exit(1)

try:
    df = pd.read_excel("sample.xlsx")
    df.columns = df.columns.str.strip()  
except FileNotFoundError:
    print("Error: sample.xlsx not found")
    sys.exit(1)

print("Columns found:", list(df.columns))  # debug

required_columns = ["Customer Name", "Product ID", "Date"]

missing = [c for c in required_columns if c not in df.columns]
if missing:
    print(f" Error: Missing required columns in spreadsheet: {missing}")
    sys.exit(1)

for _, row in df.iterrows():
    print(row["Customer Name"], row["Product ID"], row["Date"])
import argparse

# 1. Create ArgumentParser
parser = argparse.ArgumentParser(description="Document generation script")

# 2. Define command-line arguments
parser.add_argument("--template", help="Path to Word template file")
parser.add_argument("--spreadsheet", help="Path to spreadsheet file")
parser.add_argument("--output", help="Output directory")

# 3. Parse arguments
args = parser.parse_args()

# 4. Print parsed values
print("Template path:", args.template)
print("Spreadsheet path:", args.spreadsheet)
print("Output directory:", args.output)
