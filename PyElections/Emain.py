import os
import csv
import operator 

with open('houston_election_data.csv',newline="",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_header = next(csv_file)
        
        #setting variable vote count to 0
        total_vote = 0
        candidates_name = []
        #create a dictionray for candidates name and vote count
        candidates_votes = {}
        
                        
        #Counting the numbers of votes, excluding the header
        for row in csv_reader:
            total_vote = total_vote + 1

            if row[0] in candidates_votes.keys():
                candidates_votes[row[0]]=candidates_votes[row[0]] +1
            else:
                candidates_votes[row[0]] = 1

#Counting the candidates in the data set
  
candidates_result = []
votes_candidates = []

#using the dictionary key to fill each list created
for key, value in candidates_votes.items():
    candidates_result.append(key)
    votes_candidates.append(value)

poll_percent = []
for n in votes_candidates:
    poll_percent.append(round(n/total_vote*100, 1))

poll_results = list(zip(candidates_result, votes_candidates, poll_percent))

#print(poll_percent)
#print(candidates_votes)
sorted_data_names = dict(sorted(candidates_votes.items(), key = operator.itemgetter(1),reverse=True))
#print(sorted_data_names)

top2_cand = list(sorted_data_names.keys())

#testing top2 candidates list
#print(top2_cand[0])
#print(top2_cand[1])


publish_data = os.path.join('Py_Polls_Results/election_result.txt')

Results = (
f" Houston Mayor Election Results \n"
f"-------------------------------\n"
f"Total Cast Votes: {total_vote} \n"
f"-------------------------------\n"

#try to use the dictionary I built to try to ron it through a loop and give me the entire information for each candidate
    #for x, y in sorted_data_names.items():
        #z = round(((y/total_vote)*100),2)
        #f = open("election__result.txt", "a")
        #f.write(f"{x}:  {z}%  ({y}) \n")
        #f.close()
f"-------------------------------\n"
f"Advancing Candidate # 1 {top2_cand[0]} \n"
f"Advancing Candidate # 2 {top2_cand[1]} \n"
)
print(Results)

with open (publish_data, 'w') as txtfile:
    txtwriter = txtfile.write(Results)

