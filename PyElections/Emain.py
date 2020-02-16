import os
import csv

with open('houston_election_data.csv',newline="",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_header = next(csv_file)
        
        row_count = 0
        candidates_name = []

        for row in csv_reader:

            row_count = row_count + 1

            candidates = row[0]
            if candidates not in candidates_name : 
                candidates_name.append(candidates)


# Setting up the print of the information calculated
print("---------------------------------------------")
print("Total Votes")
print(row_count)
print("---------------------------------------------")

print(candidates_name)
