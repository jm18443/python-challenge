# Modules
import os
import csv
agains = "y"

while agains == "y":
# Prompt user for title lookup
    book = input("What title are you looking for? ")
  

# Set path for file
    csvpath = os.path.join("budget_data.csv")

# Set variable to check if we found the video
    found = False

# Open the CSV
    with open(csvpath, encoding='utf') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
        for row in csvreader:
                print(row[0])

            # Set variable to confirm we have found the video
                found = True
                agains = input("Would you like to try again?")


    # If the book is never found, alert the user

    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
        agains = input("Would you like to try again?")
