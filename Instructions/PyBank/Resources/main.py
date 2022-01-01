import os
import csv
#create a path with the file
Budget_data_path = os.path.join('budget_data.csv')
#create empty variables
Number_of_months = 0
Profit_Losses = []
Monthly_change = []
Changes = []
#create function for Average
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
with open(Budget_data_path, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    previous_row = 0
    for row in csvreader:
        Monthly_change.append(row[0])
        Profit_Losses.append(int(row[1]))
        if len(Changes)== 0:
            Changes.append(0)
        else:
            Changes.append(int(row[1])-previous_row)
        previous_row=int(row[1])       
# Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows
# previous_row = int(row[1])
# Number_of_months += 1
# Profit_Losses += int(row[1])
print(Profit_Losses)
print(Monthly_change)
print(Changes)
#Calculate Sum of profit
print(sum(Profit_Losses))
#Calculate Total Months
print(len(Monthly_change))
print(average(Changes[1:]))

#Greatest Increase in Profits and Greatest Decrease in Profits
print(max(Changes))
max_index=Changes.index(max(Changes))
print(Monthly_change[max_index])
print(min(Changes))
min_index=Changes.index(min(Changes))
print(Monthly_change[min_index])

#Printing results to terminal
    
print("Financial Analysis\n--------------------")
print(f'Total Months: {len(Monthly_change)}')
print(f'Total: ${sum(Profit_Losses)}')
print(f'Average Change: ${round(average(Changes[1:]),2)}')
print(f'Greatest Increase in Profits: {(Monthly_change[max_index])} (${(max(Changes))})')
print(f'Greatest Decrease in Profits: {(Monthly_change[min_index])} (${(min(Changes))})')


# exporting a text file with the results
# output_path = os.path.join('finance_analysis.csv')
# with open(output_path, 'w', newline='') as csvfile:
#      csvwriter = csv.writer(csvfile, delimiter=',')
#      csvwriter.writerow(["Financial Analysis"])
#      csvwriter.writerow(["---------------------"])
#      csvwriter.writerow(f'Total Months: {len(Monthly_change)}')
#      csvwriter.writerow(f'Total: ${sum(Profit_Losses)}')
#      csvwriter.writerow(f'Average Change: ${round(average(Changes[1:]),2)}')
#      csvwriter.writerow(f'Greatest Increase in Profits: {(Monthly_change[max_index])} (${(max(Changes))})')
#      csvwriter.writerow(f'Greatest Decrease in Profits: {(Monthly_change[min_index])} (${(min(Changes))})')


# exporting a text file with the results
financial_analysis_file = os.path.join("finance_analysis.csv.txt")
with open(financial_analysis_file, "w") as outfile:

     outfile.write("Financial_Analysis\n")
     outfile.write("-------------------------\n")
     outfile.write(f"Total Months: {len(Monthly_change)}")
     outfile.write(f"Total: ${sum(Profit_Losses)}")
     outfile.write(f"Average Change: ${round(average(Changes[1:]),2)}")
     outfile.write(f"Greatest Increase in Profits: {(Monthly_change[max_index])} (${(max(Changes))})")
     outfile.write(f"Greatest Decrease in Profits: {(Monthly_change[min_index])} (${(min(Changes))})")  