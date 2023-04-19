import csv
from decimal import Decimal, ROUND_DOWN
from pathlib import Path

csvpath = Path("Resources/election_data.csv")

#opening .csv file with election data

with open(csvpath, encoding='utf') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    reader = csv.DictReader(csvfile)

    #Reading and storing the header names

    header = reader.fieldnames 

    u_candidates = []
    candidates = []
    total_votes = int(0)

    #get total votes and candidates names

    for x in csvreader: 
        row = x[2]
        candidates.append(row)
        total_votes = total_votes + 1

    #Finding unique candidate names

    u_candidates = set(candidates) 
    u_candidates = list(u_candidates)

    #Set up a dictionary to hold the election results

    tallies = {} 
    
    votes = [0] * len(u_candidates)
    percentages = [0] * len(u_candidates)
    
    tallies["name"] = u_candidates
    tallies["votes"] = votes
    tallies["percentages"] = percentages

    #Getting the vote tally for each candidate

    for y in range(len(u_candidates)): 
        for z in candidates:
            if z == tallies["name"][y]:
                tallies["votes"][y] = tallies["votes"][y] + 1

    #Getting percetages for each candidate

    for a in range(len(u_candidates)):  
        percentages[a] = (tallies["votes"][a] / total_votes) * 100
        percentages[a] = '{0:.3f}'.format(percentages[a])

    win = max(votes)
    winner = ""
    
    #Finding the winning candidate

    for b in range(len(u_candidates)): 
        if tallies["votes"][b] == win:
            winner = tallies["name"][b]

#Printing to the terminal

print('Election Results')
print('--------------------')
print(f"Total Votes: {total_votes}")
print('--------------------')
print(f"{tallies['name'][0]}: {tallies['percentages'][0]}% ({tallies['votes'][0]})")
print(f"{tallies['name'][1]}: {tallies['percentages'][1]}% ({tallies['votes'][1]})")
print(f"{tallies['name'][2]}: {tallies['percentages'][2]}% ({tallies['votes'][2]})")
print('--------------------')
print(f"Winner: {winner}")

#Writing output .txt file

file = open('Election_Results.txt', 'w')

lines = ['Election Results','--------------------',f"Total Votes: {total_votes}",'--------------------',
         f"{tallies['name'][0]}: {tallies['percentages'][0]}% ({tallies['votes'][0]})",
         f"{tallies['name'][1]}: {tallies['percentages'][1]}% ({tallies['votes'][1]})",
         f"{tallies['name'][2]}: {tallies['percentages'][2]}% ({tallies['votes'][2]})",
         '--------------------', f"Winner: {winner}",'--------------------']

for line in lines:
    file.write(line)
    file.write('\n')
    file.write('\n')
