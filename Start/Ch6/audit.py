import pandas as pd
import sys
import os
import numpy as np

def excel_to_csv(excel_path, csv_path):
    """
    Convert an Excel file (.xlsx or .xls) to a comma-separated CSV file.
    """
    try:
        # Validate file existence
        if not os.path.isfile(excel_path):
            raise FileNotFoundError(f"Excel file not found: {excel_path}")

        # Read Excel file (first sheet by default)
        df = pd.read_excel(excel_path, sheet_name=0)

        # Save as CSV with comma delimiter
        # df.to_csv(csv_path, index=False, sep=',', encoding='utf-8')
        np.savetxt('output.txt', df.values, fmt='%s', delimiter='","')

        print(f"✅ Successfully converted '{excel_path}' to '{csv_path}'")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Example usage: python script.py input.xlsx output.csv
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_excel> <output_csv>")
        sys.exit(1)

    excel_file = sys.argv[1]
    csv_file = sys.argv[2]
    excel_to_csv(excel_file, csv_file)
