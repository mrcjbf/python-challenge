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

# createFile = input("Create a text file with output? Y or N ")

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

totalsDictionary["Khan"] = len(khanIds)
totalsDictionary["Li"] = len(liIds)
totalsDictionary["O'Tooley"] = len(otoolIds)
totalsDictionary["Correy"] = len(correyIds)

max_value = max(totalsDictionary.values())  # maximum value
max_keys = [k for k, v in totalsDictionary.items() if v == max_value] # getting all keys containing the `maximum`

print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(idsSet)}")
print("----------------------------")
# fix decimals
print(f"Khan: {round((len(khanIds)/len(idsSet))*100)}.000% ({len(khanIds)})")
print(f"Correy: {round((len(correyIds)/len(idsSet))*100)}.000% ({len(correyIds)})")
print(f"Li: {round((len(liIds)/len(idsSet))*100)}.000% ({len(liIds)})")
print(f"O'Tooley: {round((len(otoolIds)/len(idsSet))*100)}.000% ({len(otoolIds)})")
print("----------------------------")
print(f"Winner: {max_keys[0]}")
print("----------------------------")

# if createFile == "Y" or createFile == "y":
text_file = open("Output.txt", "w")
text_file.write("Election Results\n")
text_file.write("----------------------------\n")
text_file.write(f"Total Votes: {len(idsSet)}\n")
text_file.write("----------------------------\n")
text_file.write(f"Khan: {round((len(khanIds)/len(idsSet))*100)}.000% ({len(khanIds)})\n")
text_file.write(f"Correy: {round((len(correyIds)/len(idsSet))*100)}.000% ({len(correyIds)})\n")
text_file.write(f"Li: {round((len(liIds)/len(idsSet))*100)}.000% ({len(liIds)})\n")
text_file.write(f"O'Tooley: {round((len(otoolIds)/len(idsSet))*100)}.000% ({len(otoolIds)})\n")
text_file.write("----------------------------\n")
text_file.write(f"Winner: {max_keys[0]}\n")
text_file.write("----------------------------\n")
text_file.close()