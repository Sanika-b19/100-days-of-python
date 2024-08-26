# Project: Convert CSV Data to JSON Format

import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    
    # csv file
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    
    # json file
    with open(json_file, mode='w') as file:
        json.dump(data, file, indent=4)


csv_file_path = 'sample.csv'
json_file_path = 'output.json'
csv_to_json(csv_file_path, json_file_path)

print(f"CSV data from {csv_file_path} has been converted to JSON and saved in {json_file_path}.")
