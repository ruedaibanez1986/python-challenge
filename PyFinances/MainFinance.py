import os
import csv

#opening the csv file 
with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #excluding headers of the csv file
    csv_header = next(csv_file)
#Creating counters
    total_months = 0
    pnl_total = 0
    past_pnl = 0
    g_increase = 0
    l_decrease = 99999999999
    profit_change = []
    count = 0
       
    for row in csv_reader:
        #count total months in data set
        total_months = total_months + 1
        #calculate total p&l of the data set
        pnl = int(row[0])
        pnl_total += pnl
        #set a variable to count var in p&l
        monthly_profit_var = pnl - past_pnl
        past_pnl = pnl
        
        #add var to a list
        profit_change.append(monthly_profit_var)
        #average calculation 
        # print(profit_change)
        count += 1
        # var_profit_change = round(sum(profit_change)/count)
        
        # print(f"sum(profit_change)/count: {sum(profit_change/count)}")
        # print(var_profit_change)
        #determine the highes and lowest p&l change


        if (monthly_profit_var > g_increase):
            greatest_increase_month = row[1]
            g_increase = monthly_profit_var
        if (monthly_profit_var < l_decrease):
            lowest_decrease_month = row[1]
            l_decrease = monthly_profit_var
    popped_value = profit_change.pop(0)
    print(f"popped_value: {popped_value}")
    var_profit_change = round(sum(profit_change)/(count-1))
    print(f"Count-1: {count-1}")
    print(f"sum(profit_change): {sum(profit_change)}")
    print(f"len(profit_change): {len(profit_change)}")
    print(f"profit_change = {profit_change}")
#Place results in a variable as f string for formatting
Results = (
f" Financial Analysis \n"
f"-------------------------\n"
f"Total Months: {total_months} \n"
f"Total: ${pnl_total} \n"
f"Average Change: ${var_profit_change} \n"
f"Greatest Increase in Profit: {greatest_increase_month} ${g_increase} \n"
f"Greates Decrease in Profit: {lowest_decrease_month} ${l_decrease} \n"
)
#Test Results out of the format     
print(Results)


with open('profit_change.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # for value in profit_change:
    #     # using CSV library, save this list to a csv file
    writer.writerow(profit_change)

Results = (
f" Financial Analysis \n"
f"-------------------------\n"
f"Total Months: {total_months} \n"
f"Total: ${pnl_total} \n"
f"Average Change: ${var_profit_change} \n"
f"Greatest Increase in Profit: {greatest_increase_month} ${g_increase} \n"
f"Greates Decrease in Profit: {lowest_decrease_month} ${l_decrease} \n"
)
#Test Results out of the format     
print(Results)
# #create path to publish results
publish_data = os.path.join('Py_Finance_Analisis/finances_analysis.txt')
with open (publish_data, 'w') as txtfile:
    txtwriter = txtfile.write(Results)