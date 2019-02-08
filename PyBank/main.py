import os
import csv

csv_file_path = os.path.join(".", "Resources", "budget_data.csv")
monthsArray = []
netTotal = 0
avgTotal = 0
greatestIncrease = 0
greatestDecrease = 0
greatestIncMonth = ""
greatestDecMonth = ""

# createFile = input("Create a text file with output? Y or N ")

# Open and read csv
with open(csv_file_path, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row first (skip this part if there is no header)
	csv_header = next(csvfile)

	# Read through each row of data after the header
	for row in csvreader:
		currentTotal = int(row[1])
		monthsArray.append(row[0])
		netTotal = netTotal + currentTotal
		if int(row[1])>greatestIncrease:
			greatestIncrease = int(row[1])
			greatestIncMonth = row[0]
		if int(row[1])<greatestDecrease:
			greatestDecrease = int(row[1])
			greatestDecMonth = row[0]

avgTotal = netTotal/len(monthsArray)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(monthsArray)}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${round(avgTotal,2)}\n")
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDecrease})")

# if createFile == "Y" or createFile == "y":
text_file = open("Output.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("----------------------------\n")
text_file.write(f"Total Months: {len(monthsArray)}\n")
text_file.write(f"Total: ${netTotal}.00\n")
text_file.write(f"Average Change: ${round(avgTotal,2)}\n")
text_file.write(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestIncrease})\n")
text_file.write(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDecrease})\n")
text_file.close()
