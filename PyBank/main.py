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

# Open and read csv
with open(csv_file_path, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row first (skip this part if there is no header)
	csv_header = next(csvfile)
	print(f"Header: {csv_header}")
	print(f"csv reader: {csvreader}")

	# Read through each row of data after the header
	for row in csvreader:
		currentTotal = int(row[1])
		if not row[0] in monthsArray:
			monthsArray.append(row[0])
			netTotal = netTotal + currentTotal
		if int(row[1])>greatestIncrease:
			greatestIncrease = int(row[1])
			greatestIncMonth = row[0]
		if int(row[1])<greatestDecrease:
			greatestDecrease = int(row[1])
			greatestDecMonth = row[0]

avgTotal = netTotal/len(monthsArray)
		
print(f"how many months: {len(monthsArray)}")
print(f"months array: {monthsArray}")
print(f"net total: {netTotal}")
print(f"avg total: {avgTotal}")
print(f"greatest increase: {greatestIncrease} happened in: {greatestIncMonth}")
print(f"greatest decrease: {greatestDecrease} happened in: {greatestDecMonth}")
