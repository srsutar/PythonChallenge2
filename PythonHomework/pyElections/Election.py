#Import the libraries needed
import os
import csv

cvspath_read = os.path.join("")

#generate an table with columns distinct_candidates,total_votes
#accrual of total_votes
candidate_table={}
total_votes=0
with open('Elections2.csv') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        total_votes+=1
        if row[0] not in candidate_table.keys():
            candidate_table[row[0]]=1
        else:
            for key in candidate_table.keys():
                if key==row[0]:
                    candidate_table[key]+=1
#    print(candidate_table)
#print(total_votes)

#Sort by number of votes
sorted_candidate_tuples=sorted(candidate_table.items(), key=lambda candidate: candidate[1],reverse=True)
#print(sorted_candidate_tuples)

#Print summary
print("Houston Mayoral Election Results")
print("-----------------------------------------")
print(f"Total Cast Votes: {total_votes}")
print("-----------------------------------------")

for row in sorted_candidate_tuples:
    print(f"{row[0]}: {round(int(row[1])/total_votes*100,2)}% ({row[1]})")
print("-----------------------------------------")
print(f"1'st Advancing Candidate: {sorted_candidate_tuples[0][0]}")
print(f"2'nd Advancing Candidate: {sorted_candidate_tuples[1][0]}")
print("-----------------------------------------")
#Write into file Results.csv
cvspath_write=os.path.join("Results.csv")
with open(cvspath_write,"w",newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Candidate Name","Total Votes[#]","Total Votes[%]"])
    for row in sorted_candidate_tuples:
        csvwriter.writerow([row[0],row[1],round(int(row[1])/total_votes*100,2)])
        print([row[0],row[1],round(int(row[1])/total_votes*100,2)])