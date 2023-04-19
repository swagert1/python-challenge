import csv
from decimal import Decimal, ROUND_DOWN
import math
from pathlib import Path

csvpath = Path("Resources/budget_data.csv")

#csvpath = "C:\\Users\\gmich\\OneDrive\\Desktop\\UofM_Bootcamp\\Python\\Week_1\\Starter_Code\\PyBank\\Resources\\budget_data.csv"

#Reading in .csv file with financial data

with open(csvpath, encoding='utf') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    reader = csv.DictReader(csvfile)

    #Reading and storing the header names

    header = reader.fieldnames 

    #Setting up variables to hold reported values

    total_profit = float(0) 
    max_profit_change = float(0)
    max_profit_date = str(0)
    max_loss_change = float(0)
    max_loss_date = str(0)
    prev_profit = float(0)
    profit_change = float(0)
    total_profit_change = float(0)
    num_months = int(0)
    average_change = float(0)

    for x in csvreader:
    
        date = x[0]
        profit = float(x[1])

        #Finding the profit changes and summing them

        if num_months >= 1: 
            profit_change = profit - prev_profit
            total_profit_change = total_profit_change + profit_change
        
        prev_profit = profit
        
        total_profit = total_profit + profit

        #Finding max/min profit changes

        if profit_change > max_profit_change: 
            max_profit_change = profit_change
            max_profit_date = date
        elif profit_change < max_loss_change:
            max_loss_change = profit_change
            max_loss_date = date

        num_months = num_months + 1

#Formatting output values

total_profit=math.trunc(total_profit) 
max_profit_change=math.trunc(max_profit_change)
max_loss_change=math.trunc(max_loss_change)
average_change = total_profit_change/(num_months - 1)
average_change = Decimal(str(average_change)).quantize(Decimal('0.01'))

#Printing analysis to the terminal

print("Financial Analysis")
print('--------------------')
print(f"Total Moths: {num_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest increase in profits: {max_profit_date} (${max_profit_change})")
print(f"Greatest decrease in profits: {max_loss_date} (${max_loss_change})")

#Writing results to .txt file

file = open('Financial_Analysis.txt', 'w')

lines = ['Financial Analysis','--------------------',f"Total Months: {num_months}",
         f"Total: ${total_profit}",
         f"Average Change: ${average_change}",
         f"Greatest increase in profits: {max_profit_date} (${max_profit_change})",
         f"Greatest decrease in profits: {max_loss_date} (${max_loss_change})"]

for line in lines:
    file.write(line)
    file.write('\n')
    file.write('\n')





