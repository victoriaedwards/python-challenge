import os

# Module for reading CSV files
import csv

csvpath = os.path.join('/Users/Victoria/bootcamp/CU-NYC-DATA-PT-10-2019-U-C/Homework/03-Python/Instructions/PyBank/Resources', 'budget_data.csv')


monthCount=0
totalProfit=0
totalLoss=0
greatestProfit=0
greatestLoss=0
rowCount=0
deltaPnL=0
sumdeltaPnL=0
prevMonthlyPnL=0
greatestIncrease=0
greatestDecrease=0
greatestIncreaseMonth=" "
greatestDecreaseMonth= " "


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #print(row[1])
        monthCount=monthCount+1

        month=row[0]
        monthlyPnL= int(row[1])
        
        if rowCount > 0:
            deltaPnL= monthlyPnL-prevMonthlyPnL
            sumdeltaPnL=sumdeltaPnL+deltaPnL

        if monthlyPnL > 0:
           totalProfit=totalProfit+monthlyPnL
        else:
            totalLoss=totalLoss+monthlyPnL

        if monthlyPnL-prevMonthlyPnL > greatestIncrease:
                greatestIncrease=monthlyPnL-prevMonthlyPnL
                greatestIncreaseMonth=month

        if monthlyPnL-prevMonthlyPnL < greatestDecrease:
                greatestDecrease=monthlyPnL-prevMonthlyPnL
                greatestDecreaseMonth=month
                
        prevMonthlyPnL=monthlyPnL
        rowCount=rowCount+1

    print("                     ")
    print("Financial Analysis")
    print("---------------------------") 
    print(f"Total months: {monthCount}")
    netProfit=totalProfit+totalLoss
    print(f"Net profit: ${netProfit}")
    avgChange=round(sumdeltaPnL/(monthCount-1),2)
    print(f"Average change: ${avgChange}")
    #print(f"Greatest profit: {greatestProfit}")
    #print(f"Greatest loss: {greatestLoss}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth}  (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth}  (${greatestDecrease})")
    
    #print to txt file
    with open("Pybank_output.txt", "w") as f:
        print("                     ", file=f)
        print("Financial Analysis", file=f)
        print("---------------------------", file=f) 
        print(f"Total months: {monthCount}", file=f)
        netProfit=totalProfit+totalLoss
        print(f"Net profit: ${netProfit}", file=f) 
        avgChange=round(sumdeltaPnL/(monthCount-1),2)
        print(f"Average change: ${avgChange}", file=f) 
        #print(f"Greatest profit: {greatestProfit}")
        #print(f"Greatest loss: {greatestLoss}")
        print(f"Greatest Increase in Profits: {greatestIncreaseMonth}  (${greatestIncrease})", file=f) 
        print(f"Greatest Decrease in Profits: {greatestDecreaseMonth}  (${greatestDecrease})", file=f) 
    