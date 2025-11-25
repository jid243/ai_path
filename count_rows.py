# count_rows.py
import csv
import sys

import os
print("Current directory:", os.getcwd())
print("Files here:", os.listdir())

def count_rows(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return sum(1 for _ in reader)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_rows.py path/to/file.csv")
    else:
        path = sys.argv[1]
        print(f"Rows in {path}: {count_rows(path)}")
