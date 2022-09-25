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


  

# Set path for file
csvpath = os.path.join("budget_data.csv")



# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        csv_header = next(csvreader)

    # Loop through looking for the video
        for row in csvreader:
                total_months= total_months + 1
                total = int(row[1]) + total

                if int(row[1]) > high:
                    high = int(row[1])
                if low > int(row[1]): 
                    low = int(row[1])


        changes = total/total_months

print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {total_months}")
print(f"Total ${total}")
print(f"Average Change: ${changes}")
print(f"Greatest Increase in Profits: {high_months} {high}")
print(f"Greatest Decrease in Profits: {low_months} {low}")

txtpath = os.path.join("..","..","Analysis","Analysis_Bank.txt")

with open(txtpath, 'w') as f:
    
    f.write(f"Financial Analysis")
    f.write('\n'f"--------------------------")
    f.write('\n'f"Total Months: {total_months}")
    f.write('\n'f"Total ${total}")
    f.write('\n'f"Average Change: ${changes}")
    f.write('\n'f"Greatest Increase in Profits: {high_months} {high}")
    f.write('\n'f"Greatest Decrease in Profits: {low_months} {low}")
        

