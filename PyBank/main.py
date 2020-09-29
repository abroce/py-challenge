import csv

inputfile='Resources/budget_data.csv'
outputfile='Analysis/Budget_Analysis.txt'

profit_loss=[]
pl_summary={}

with open(inputfile, newline='') as csvfile:
    # reads and then splits the data by commas and places in a string variable budget_reader
    budget_reader=csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(budget_reader)
    
    total=0
    total_months=0
    # Converts the budget_reader string to a profit_loss list
    for line in budget_reader:
        profit_loss.append(line)
        # The total net amount of "Profit/Losses" over the entire period
        total+=int(line[1])
        # The total number of months included in the dataset
        total_months+=1
       
    subtracted=0
    TotalM=0
    AvgM=0
    # Initialize max increase and max decrease values with latest increase/decrease value
    max_decrease=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    max_increase=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    # Compute the change in "Profit/Losses" between months over the entire period
    # by iterating (backwards) from latest month-year to the earliest
    for i in range(total_months,1,-1): # stops when i is 2
        subtracted=int(profit_loss[i-1][1])-int(profit_loss[i-2][1])
        # Find the Greatest Increase (max_increase) and Greatest Decrease (max_decrease)
        if subtracted < max_decrease:
            min_month_yr=profit_loss[i-1][0]
            max_decrease=subtracted
        elif subtracted > max_increase:
            max_increase=subtracted
            max_month_yr=profit_loss[i-1][0]
        # Total amount change in "Profit/Losses" between months over the entire period
        TotalM=TotalM+subtracted
    #The average change in "Profit/Losses" between months over the entire period    
    AvgM=TotalM/(total_months-1)
        

text_file=open(outputfile,"w")
text_file.write('Financial Analysis')
print('Financial Analysis')
text_file.write('\n----------------------------')
print('----------------------------')
text_file.write('\nTotal Months: '+str(total_months))
print('Total Months: '+str(total_months))
text_file.write('\nTotal: $'+str(total))
print('Total: $'+str(total))
text_file.write('\nAverage  Change: $'+str(round(AvgM,2)))
print('Average  Change: $'+str(round(AvgM,2)))
text_file.write('\nGreatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
text_file.write('\nGreatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
text_file.close()