import os
import csv
import operator

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
	if cand=="Khan":
		totalsDictionary[cand] = len(khanIds)
	if cand=="Li":
		totalsDictionary[cand] = len(liIds)
	if cand=="O'Tooley":
		totalsDictionary[cand] = len(otoolIds)
	if cand=="Correy":
		totalsDictionary[cand] = len(correyIds)

print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(idsSet)}")
print("----------------------------")
# fix decimals
print(f"Khan: {round((len(khanIds)/len(idsSet))*100)}%, total votes = {len(khanIds)}")
print(f"Li: {round((len(liIds)/len(idsSet))*100)}%, total votes = {len(liIds)}")
print(f"O'Tooley: {round((len(otoolIds)/len(idsSet))*100)}%, total votes = {len(otoolIds)}")
print(f"Correy: {round((len(correyIds)/len(idsSet))*100)}%, total votes = {len(correyIds)}")
print("----------------------------")

max_value = max(totalsDictionary.values())  # maximum value
max_keys = [k for k, v in totalsDictionary.items() if v == max_value] # getting all keys containing the `maximum`

print(f"Winner: {max_keys[0]}")
print("----------------------------")