# Exercise 2: Filter CSV Data Based on Conditions

import csv
from datetime import datetime

def filter_employees(csv_file, output_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        with open(output_file, mode='w', newline='') as output:
            fieldnames = csv_reader.fieldnames
            csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in csv_reader:
                start_date = datetime.strptime(row['start_date'], '%Y-%m-%d')
                if (datetime.now() - start_date).days >= 730:  # 2 years in days
                    csv_writer.writerow(row)

 filter_employees('employees.csv', 'filtered_employees.csv')
