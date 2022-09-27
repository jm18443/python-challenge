# Modules
import os
import csv
agains = "y"

total_months = 0
total = 0
changes = 0
high_months = " "
low_months = " "
high = 0
low = 0
need = 0
summy = 0
hold = 0
grab = 0

profit_change = []
total_profit = []

# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")



# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        csv_header = next(csvreader)

    # Loop through looking for the video
        for row in csvreader:
                total_months= total_months + 1
                total = int(row[1]) + total
                total_profit.append(int(row[1]))

                if hold == 0:
                    hold = int(row[1])
                else:
                    grab = int(row[1])
                    summy = grab - hold
                    if summy > high:
                        high = summy
                        high_months = row[0]
                    if summy < low:
                        low = summy
                        low_months = row[0]
                    need = summy + need
                    hold = grab

        changes = need/(total_months-1)

print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {total_months}")
print(f"Total ${total}")
print(f"Average Change: ${round(changes,2)}")
print(f"Greatest Increase in Profits: {high_months} ${high}")
print(f"Greatest Decrease in Profits: {low_months} ${low}")

txtpath = os.path.join("..","Analysis","Analysis_Bank.txt")

with open(txtpath, 'w') as f:
    
    f.write(f"Financial Analysis")
    f.write('\n'f"--------------------------")
    f.write('\n'f"Total Months: {total_months}")
    f.write('\n'f"Total ${total}")
    f.write('\n'f"Average Change: ${changes}")
    f.write('\n'f"Greatest Increase in Profits: {high_months} {high}")
    f.write('\n'f"Greatest Decrease in Profits: {low_months} {low}")
        

