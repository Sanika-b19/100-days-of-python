# Exercise 3: Merge Multiple CSV Files

import csv

def merge_csv(files, output_file):
    merged_data = []
    for file in files:
        with open(file, mode='r') as f:
            csv_reader = csv.DictReader(f)
            if not merged_data:
                merged_data.append(csv_reader.fieldnames)
            for row in csv_reader:
                merged_data.append(row.values())
    
    with open(output_file, mode='w', newline='') as output:
        csv_writer = csv.writer(output)
        csv_writer.writerows(merged_data)

merge_csv(['sales_jan.csv', 'sales_feb.csv'], 'merged_sales.csv')
