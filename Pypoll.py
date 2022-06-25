# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1

        # Get the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list if not already existing.
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

for candidate_name in candidate_votes:
    
    # Retrive vote count of a candidate.
    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes) / float(total_votes) * 100

    # Print each candidate, their voter count, and percentage to the terminal.
    print(f'{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n')

    # Determine winning vote count, winning percentage, and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

# Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f'--------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'--------------------------\n')

print(winning_candidate_summary)
