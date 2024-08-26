# Exercise 1: Read and Summarize CSV Data

import csv

def summarize_sales(csv_file):
    sales_summary = {}
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = row['product']
            total = int(row['quantity']) * float(row['price'])
            if product in sales_summary:
                sales_summary[product] += total
            else:
                sales_summary[product] = total
    return sales_summary

print(summarize_sales('sales.csv'))
