import pandas as pd
import math
import os

# Configuration
ROWS_PER_CHUNK = 998              # Number of rows per split file
OUTPUT_FOLDER = "Split_Files_CSV" # Folder to store output files

# 1: Find the first Excel or CSV file in the current directory
def find_input_file():
    for file in os.listdir():
        # Check for both .xlsx and .csv extensions
        if file.lower().endswith(('.xlsx', '.csv')):
            return file
    return None

# 2: Load the file and split it into parts
def split_data():
    print("Searching for Input file (Excel or CSV)...")

    input_file = find_input_file()

    if not input_file:
        print("Error: No compatible file (.xlsx or .csv) found.")
        return

    print(f"File found: {input_file}")
    print("Loading file. Please wait...")

    # Load the file into a DataFrame based on extension
    try:
        if input_file.lower().endswith('.csv'):
            # Read CSV file
            df = pd.read_csv(input_file)
        else:
            # Read Excel file
            df = pd.read_excel(input_file)
            
    except Exception as e:
        print(f"Error while reading file: {e}")
        return

# 3: Calculate total rows and number of required split files
    total_rows = len(df)
    total_parts = math.ceil(total_rows / ROWS_PER_CHUNK)

    print(f"Total rows in file: {total_rows}")
    print(f"Splitting into {total_parts} files ({ROWS_PER_CHUNK} rows per file)")

# 4: Create output folder if it does not exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 5: Split the data and save each part as a new CSV file
    for part in range(total_parts):
        start_row = part * ROWS_PER_CHUNK
        end_row = start_row + ROWS_PER_CHUNK

        # Extract the required rows
        split_df = df.iloc[start_row:end_row]

        # Generate output file name
        output_file = f"{OUTPUT_FOLDER}/split_part_{part + 1}.csv"

        # Save as CSV regardless of input format
        split_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    print("File split completed successfully.")

# 6: Run the script automatically
split_data()