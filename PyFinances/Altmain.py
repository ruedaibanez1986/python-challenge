#import modules
import os
import csv
import statistics

#creating trackers

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)

#Creating counters
    total_months = 0
    pnl_total = 0
    past_pnl = 0
    g_increase = 0
    l_decrease = 99999999
    profit_change = []

       
    for row in csv_reader:
        total_months = total_months + 1
        pnl_total += int(row[0])
        monthly_profit_var = int(row[0]) - past_pnl
        past_pnl = int(row[0])
        profit_change.append(monthly_profit_var)
        var_profit_change = round(sum(profit_change)/total_months)

        if (monthly_profit_var > g_increase):
            greatest_increase_month = row[1]
            g_increase = monthly_profit_var
        if (monthly_profit_var < l_decrease):
            lowest_decrease_month = row[1]
            l_decrease = monthly_profit_var
Results = (
f" Financial Analysis \n"
f"-------------------------\n"
f"Total Months: {total_months} \n"
f"Total: ${pnl_total} \n"
f"Average Change: ${var_profit_change} \n"
f"Greatest Increase in Profit: {greatest_increase_month} ${g_increase} \n"
f"Greates Decrease in Profit: {lowest_decrease_month} ${l_decrease} \n"
)


publish_data = os.path.join('py_finance_sanalisis/finance_data_results.txt')

with open(publish_data, 'w') as txtfile:
    txtwriter = txtfile.write(Results)
    



        



 #Test Results out of the format     
print(Results)
print("----------------------")
print("----------------------")
print("----------------------")
print("Total Months")
print(total_months)
print("----------------------")
print("Total P&L")
print(pnl_total)
print("-----------------------")
print(var_profit_change)



