import os
import csv

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)

    row_count = 0
    pnl_total = 0
    

    for row in csv_reader:
        row_count = row_count + 1
        pnl_total += int(row[0])
    





print("----------------------")
print("Total Months")
print(row_count)
print("----------------------")
print("Total P&L")
print(pnl_total)
print("-----------------------")

