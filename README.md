# Analysis of Colorado Congressional Election Votes

## Election Audit Overview:
### Background:
A U.S. congressional race was just held in a preceint in Colorado. A Colorado Board of Elections employee named Tom is needing help with creating a vote count report to certify the results. This is normally done in Excel but Tom's manager wants a more automated process using Python.

### Purpose:
The purpose of this election audit analysis is to verify the total votes counted, the breakdown by votes by county, and the breakdown by candidate to verify the winner of the election just held. Provided this Python analysis is successful, this process will also be used to audit other elections.

## Election-Audit Results:

- number of votes cast
- breakdown of # votes and % of total for each county
- which county had larges # of votes
- breakdown of # votes and % of total for each candidate
- which candidate won, their vote count, and their % of total votes

Python code:
```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')
# Add a variable to save the file to a path.
file_to_save = os.path.join('analysis','election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
highest_turnout_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes +=1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f'{county_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(county_results)   

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):

            winning_county_count = votes
            highest_turnout_county = county_name
            winning_county_percentage = vote_percentage
            
    # 7: Print the county with the largest turnout to the terminal.
    highest_turnout_county_summary = (
        f'--------------------------\n'
        f'Largest County Turnout: {highest_turnout_county}\n'
        f'--------------------------\n')

    print(highest_turnout_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(highest_turnout_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```
## Pasted from kickstarter to show formatting:
- Outcomes vs Launch Date Conclusions:
    1. When all years are looked at together, the best time for a theater kickstarter campaign is late Spring/early Summer. This is the time of year when the likelihood of success is highest. The month of May appeared the most popular month for total theater kickstarters with the number of successful campaigns particularly pronounced. Roughly 2/3 of the total campaigns launched in May were successful.
    2. It appears to be a bad decision to launch a theater kickstarter in the month of December. The number of successes and failures are roughly even. This makes logical sense as most people are busy with holiday festivities and can be financially strapped based on other gift or donation commitments common during the holidays.

- Outcomes vs Goals Conclusions:
    1. It is recommended to keep your fundraising goals modest to give your campaign the highest likelihood of success. Close to 3 out of 4 fundraisers with goals under $5,000 are successful.

- Dataset Limitations:
    - Using this dataset in 2022 to analyze outcomes by launch date raises some concerns. There appears to be no theater data beyond the year of 2017. This is five years ago and things may have changed since then. Ideally more recent data would be included.
    - Addi

## Election Audit Summary:

### Proposal for use in future elections
Benefit over excel, why it can be used, at least two examples of can be modified for other elections

![VBA_Challenge_2017](https://github.com/bfox87/stock-analysis/blob/main/Resources/VBA_Challenge_2017.PNG)

![VBA_Challenge_2018](https://github.com/bfox87/stock-analysis/blob/main/Resources/VBA_Challenge_2018.PNG)
