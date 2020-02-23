#import modules
import os
import csv
from statistics import mean



#opening the csv file 
with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #excluding headers of the csv file
    csv_header = next(csv_file)

    
#Creating counters
    total_months = 0
    pnl_total = []
    past_pnl = 0
    g_increase = 0
    l_decrease = 99999999
    profit_change = []
    pnl_var = []

    
    for row in csv_reader:
        #count total months in data set
        total_months = total_months + 1
        #calculate total p&l of the data set 
        pnl_total.append(row[0])
        past_pnl = int(row[0])

    for i in range (len(pnl_total)):

        if i != 0:
            pnl_var.append(int(pnl_total[i])-int(pnl_total[i-1]))

             
     #Testing if I am adding the var to the determing list   
    #print(pnl_var)

    max_limit = max(pnl_var)
    min_limit = min(pnl_var)
    avg_change = mean(pnl_var)
    print("-------------------------------")
    print ("Financial Analysis")
    print("-------------------------------")
    print("Total Months")
    print(total_months)
    print("-------------------------------")
    print("Average Change")
    print("-------------------------------")
    print (avg_change)
    print("Greatest Increase in Profit")
    print(max_limit)
    print("Greatest Dcrease in Profit")
    print(min_limit)
    
    




    