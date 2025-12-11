import csv
import sys

csv.field_size_limit(sys.maxsize)

target_complexity = "O(n^3)"
count = 0
results = []

try:
    with open('complexity_results.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['complexity'] == target_complexity:
                count += 1
                results.append(row)

    print(f"Total count: {count}")
    for res in results:
        print(f"{res['file_path']}|{res['start_line']}|{res['name']}")

except Exception as e:
    print(f"Error: {e}")
