# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

#  ```text
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

#----------------------------------------------------------------------------------------------------
#Import declaration

import os
import csv



#---------------------------------------------------------------------------------------------------
#Get File input name
election_data_file = os.path.join("..", "PyPoll", "election_data.csv")



#--------------------------------------------------------------------------------------------------
#Declare and initialize variables:

#variable to count total votes casted
total_votes = 0

#variable to determine candidate w/ most popular votes
most_votes = 0

#variable to take in the count of votes for each candidate
candidate_vote_count = {}

#variable to determine the percent of votes for each candidate
candidate_vote_percent = {}

#string variable to hold the popular vote winner
winner = ""

#-----------------------------------------------------------------------------------------------------------------

#Process data
with open(election_data_file, newline="") as election_results_csv_file:
    csv_file = csv.reader(election_results_csv_file)

    #First skip reading the first row header: "Voter_ID", "County", "Candidate"
    Header = next(csv_file)

    #Next count the number of total votes and votes per candidate
    for row in csv_file:
        #assign 'candidate' as variable to next row column 2
        candidate = row[2]
        #find total votes casted by incrementing total_votes by 1 for each instances of column 2
        total_votes += 1

        #if candidate is not in candidate_vote_count variable... add the candidate name and 1 vote for candidate
        if candidate not in candidate_vote_count:
            candidate_vote_count[candidate] = 1

        #else if the candidate is already there add a vote to that candidate

        else:
            candidate_vote_count[candidate] += 1
    #----------------------------------------------------------------------------------------------------------------
    #Process results now stored in candidate_vote_count

    for candidate in candidate_vote_count:
        #Determine the percent of votes casted for each candidate and store results in candidate_vote_percent
        # take the total votes for each candidate divide by total votes casted then mult by 100 for %
        candidate_vote_percent[candidate] = (candidate_vote_count[candidate]/total_votes) * 100


        #Determine the overall winner
        #if the total candidate votes is greatest, then assign that candidate as the winner
        if candidate_vote_count[candidate] > most_votes:
            most_votes = candidate_vote_count[candidate]
            winner = candidate

#------------------------------------------------------------------------------------------------------------------------

#Create the report to display all data gathered from above

#Create a string variable to store all candidate voting information
candidate_results = ""

#for each candidate string together voting results
for candidate in candidate_vote_count:
    candidate_results = candidate_results + f" {candidate}:{candidate_vote_percent[candidate]: .2f}%" \
                                            f" ({candidate_vote_count[candidate]})"
#-----------------------------------------------------------------------------------------------------------------
#Display summary of results

summary_results = f""" Election Results 
------------------------------------------
Total Votes: {total_votes}
-------------------------------------------
{candidate_results}
-------------------------------------------
Winner: {winner}

-------------------------------------------
"""

#Print out results above
print(summary_results)

#------------------------------------------------------------------------------------------------------------------
#open output file and write in results


#Set variable for output file
results_output_file = os.path.join("election_results.txt")

#Open the output file

with open(results_output_file, "w", newline="") as textfile:
    writer = textfile.write(summary_results)

