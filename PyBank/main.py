import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

csvpath = os.path.join('Resources','budget_data.csv')

month = []
profit_loss = []

month_change = []
change = 0
last_month = 867884

greatest_profit = 0
greatest_profit_month = 0
last_months_profit = 0

greatest_loss = 0
greatest_loss_month = 0
last_months_loss = 0

with open(csvpath, "r", encoding="utf8") as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))

        change = int(row[1]) - last_month
        month_change.append(change) 
        last_month = int(row[1])

        if int(row[1]) - last_months_profit > greatest_profit:
            greatest_profit = int(row[1]) - last_months_profit
            greatest_profit_month = row[0]

        last_months_profit = int(row[1])


        if int(row[1]) - last_months_loss < greatest_loss:
            greatest_loss = int(row[1]) - last_months_loss
            greatest_loss_month = row[0]
        
        last_months_loss = int(row[1])

    print("Financial Analysis")
    total_month = len(month)
    print("Total Months: " + str(total_month))
    average_change = round(sum(month_change)/(len(month_change)-1),2)
    print("Average Change: $" + str(average_change))
    total_profit_loss = sum(profit_loss)
    print("Total: $" +str(total_profit_loss))
    print("Greatest Increase in Profits: " + str(greatest_profit_month) + " ($" +str(greatest_profit)+ ")")
    print("Greatest Decrease in Profits: " + str(greatest_loss_month) + " ($" +str(greatest_loss)+ ")")

    output_file = os.path.join("Analysis","finanical_analysis.txt")
    
    with open(output_file, 'w') as f:
        print("Financial Analysis", file=f)  
        print("Total Months: " + str(total_month), file=f)
        print("Average Change: $" + str(average_change), file=f)
        print("Total: $" +str(total_profit_loss), file=f)
        print("Total: $" +str(total_profit_loss), file=f)
        print("Greatest Increase in Profits: " + str(greatest_profit_month) + " ($" +str(greatest_profit)+ ")", file=f)
        print("Greatest Decrease in Profits: " + str(greatest_loss_month) + " ($" +str(greatest_loss)+ ")", file=f)
       
       
       
       