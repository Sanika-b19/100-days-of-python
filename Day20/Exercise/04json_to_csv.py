# Exercise 4: Convert JSON to CSV

import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, mode='r') as file:
        data = json.load(file)
    
    with open(csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data[0].keys())  
        for entry in data:
            csv_writer.writerow(entry.values())

json_to_csv('products.json', 'products.csv')
