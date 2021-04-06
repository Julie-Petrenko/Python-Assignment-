import os
import csv


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

csvpath = os.path.join('Resources','election_data.csv')

total_candidate = []
candidate = []

with open(csvpath, "r", encoding="utf8") as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')

    next(csvreader)

    for row in csvreader:

        total_candidate.append(row[2])

    for i in total_candidate:
        if i not in candidate:
            candidate.append(i)

print("Election Results")
total_votes = len(total_candidate)
print("Total Votes: " + str(total_votes))

candidate_1 = str(candidate[0])
candidate_count_1 = total_candidate.count(candidate[0])
candidate_1_percent = round((candidate_count_1 / total_votes *100), 3)
print(str(candidate_1) + ": " + str(candidate_1_percent) +"%  (" + str(candidate_count_1) +")")

candidate_2 = str(candidate[1])
candidate_count_2 = total_candidate.count(candidate[1])
candidate_2_percent = round((candidate_count_2 / total_votes *100), 3)
print(str(candidate_2) + ": " + str(candidate_2_percent) +"%  (" + str(candidate_count_2) +")")

candidate_3 = str(candidate[2])
candidate_count_3 = total_candidate.count(candidate[2])
candidate_3_percent = round((candidate_count_3 / total_votes *100), 3)
print(str(candidate_3) + ": " + str(candidate_3_percent) +"%  (" + str(candidate_count_3) +")")

candidate_4 = str(candidate[3])
candidate_count_4 = total_candidate.count(candidate[3])
candidate_4_percent = round((candidate_count_4 / total_votes *100), 3)
print(str(candidate_4) + ": " + str(candidate_4_percent) +"%  (" + str(candidate_count_4) +")")


winner = candidate_1
candidate_count_winner = candidate_count_1

if candidate_count_2 > candidate_count_winner:
    winner = candidate_2

if candidate_count_3 > candidate_count_winner:
    winner = candidate_3

if candidate_count_4 > candidate_count_winner:
    winner = candidate_4

print("Winner: " + winner)

output_file = os.path.join("Analysis","election_results.txt")
    
with open(output_file, 'w') as f:
    print("Election Results", file=f)
    print("Total Votes: " + str(total_votes), file=f)
    print(str(candidate_1) + ": " + str(candidate_1_percent) +"%  (" + str(candidate_count_1) +")", file=f)
    print(str(candidate_2) + ": " + str(candidate_2_percent) +"%  (" + str(candidate_count_2) +")", file=f)
    print(str(candidate_3) + ": " + str(candidate_3_percent) +"%  (" + str(candidate_count_3) +")", file=f)
    print(str(candidate_4) + ": " + str(candidate_4_percent) +"%  (" + str(candidate_count_4) +")", file=f)
    print("Winner: " + winner, file=f)

