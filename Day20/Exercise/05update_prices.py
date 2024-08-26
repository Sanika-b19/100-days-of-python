# Exercise 5: Update a CSV File

import csv

def update_prices(csv_file, output_file, percentage):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        with open(output_file, mode='w', newline='') as output:
            fieldnames = csv_reader.fieldnames
            csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in csv_reader:
                row['price'] = str(round(float(row['price']) * (1 + percentage/100), 2))
                csv_writer.writerow(row)

update_prices('products.csv', 'updated_products.csv', 10)
