# importing module 
import os
import csv

# defining the path for file
csvpath = os.path.join('Resources', 'budget_data.csv')
analysis_path = os.path.join('Analysis','analysis.txt' )

# for total months, net profit/loss, changes over the period, greatest increase and decrease
total_months = 0
net_total_profit = 0
changes_over_period = []
prev_net = 0
greatest_increase = ["",0]
greatest_decrease = ["",999999999]

# opening budget_data.csv file to read
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
# calculating total number of votes and profit/loss
    for row in csvreader:
        total_months = total_months + 1
        net_total_profit += int(row[1])
        
        net_chg = int(row[1]) - prev_net
        prev_net = int(row[1])
        changes_over_period += [net_chg]
# for greatest increase and decrease over
        if (net_chg > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_chg     
            
        if (net_chg < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_chg 

# file to write in 
output_file = "Analysis/analysis2.txt"
with open(output_file, "w") as text_file:
   analysis = (f"""
   ----------------------------------
   Financial Analysis
   -----------------------------
   Total Months: {total_months}
   Total: {net_total_profit}
   {greatest_increase[0]},{greatest_increase[1]}
   """)
   text_file.write(analysis)
   
   changes_over_period.pop(0)
   average =sum(changes_over_period)/len(changes_over_period)

   text_file.write(f'Average Change: {average}\n') 
   text_file.write(f'Greatest Increase in profits:{greatest_increase[0]},{greatest_increase[1]}\n')
   text_file.write(f'Greatest Decrease in Profits:{greatest_decrease[0]},{(greatest_decrease[1])}')