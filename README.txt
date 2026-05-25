====================================
      Excel / CSV File Splitter
====================================


This tool splits a large Excel (.xlsx) OR CSV (.csv) file
into multiple smaller CSV files automatically.


--------------------
REQUIREMENT
--------------------
1. Install Python from: https://www.python.org/downloads/
2. During Python installation, "Add Python to PATH" must be enabled.
3. Required Python libraries:
   - pandas
   - openpyxl
If not installed, run this command once: pip install pandas openpyxl


--------------------
HOW TO USE
--------------------
1. Copy the Excel (.xlsx) OR CSV (.csv) file
   you want to split into this folder.
2. Make sure ONLY ONE input file is in the folder.
3. Double-click: Run.bat
4. Wait until the process finishes.


--------------------
CUSTOMIZATION:
--------------------
- To change the number of rows per split file:
  1. Open the script in a text editor.
  2. Find the line: ROWS_PER_CHUNK = 998
  3. Change 998 to your desired number of rows.


--------------------
WHAT THIS TOOL DOES
--------------------
- Automatically finds the Excel or CSV file.
- Reads all rows in the file.
- Splits the file into parts of 998 rows.
- Saves all output files as CSV.


--------------------
OUTPUT
--------------------
- A folder named "Split_Files_CSV" will be created.
- Split files will be saved inside that folder.
- Each file contains up to 998 rows.

Example:
Split_Files_CSV
  |-- split_part_1.csv
  |-- split_part_2.csv
  |-- split_part_3.csv


--------------------
IMPORTANT
--------------------
- Supported input formats: .xlsx and .csv only.
- Keep only ONE input file in the folder.
- Do NOT rename or delete the Python or BAT files.
- Large files may take a few minutes to process.


--------------------
UNINSTALL (OPTIONAL)
--------------------
- To uninstall Python:
  Go to Start > Settings > Apps > Installed Apps,
  search for "Python" and uninstall it.

- To uninstall libraries:
  Run this command in CMD:
  pip uninstall pandas openpyxl
