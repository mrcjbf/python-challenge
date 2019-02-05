import os
import csv

csv_file_path = os.path.join(".", "Resources", "election_data.csv")
voteridsArray = []
allVotedCandidates = []
totalsDictionary = {}
khanIds = []
liIds = []
otoolIds = []
correyIds = []

# Open and read csv
with open(csv_file_path, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row first (skip this part if there is no header)
	csv_header = next(csvfile)
	print(f"Header: {csv_header}")
	print(f"csv reader: {csvreader}")

	for row in csvreader:
		# if not row[0] in voteridsArray:
		# voteridsArray.append(row[0])
		allVotedCandidates.append(row[2])
		if row[2]=="Khan":
			khanIds.append(row[0])
		if row[2]=="Li":
			liIds.append(row[0])
		if row[2]=="O'Tooley":
			otoolIds.append(row[0])
		if row[2]=="Correy":
			correyIds.append(row[0])

voteridsArray = khanIds+liIds+otoolIds+correyIds
idsSet = list(set(voteridsArray))
candidatesSet = list(set(allVotedCandidates))

for cand in candidatesSet:
	totalsDictionary[cand] = 0

print(f"total votes: {len(idsSet)}")
print(f"all cand receiving votes: {candidatesSet}")
print(f"totals dict: {totalsDictionary}")
print(f"khan perc: {(len(khanIds)/len(idsSet))*100}%, total votes = {len(khanIds)}")
print(f"li perc: {(len(liIds)/len(idsSet))*100}%, total votes = {len(liIds)}")
print(f"o'tooley perc: {(len(otoolIds)/len(idsSet))*100}%, total votes = {len(otoolIds)}")
print(f"correy perc: {(len(correyIds)/len(idsSet))*100}%, total votes = {len(correyIds)}")