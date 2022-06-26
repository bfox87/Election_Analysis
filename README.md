# Analysis of Colorado Congressional Election Votes

## Election Audit Overview:
### Background:
A U.S. congressional race was just held in a precinct in Colorado. A Colorado Board of Elections employee named Tom is needing help with creating a vote count report to certify the results. This is normally done in Excel but Tom's manager wants a more automated process using Python.

### Purpose:
The purpose of this election audit analysis is to verify the total votes counted, the breakdown by votes by county, and the breakdown by candidate to verify the winner of the election just held. Provided this Python analysis is successful, this process will also be used to audit other elections.

## Election-Audit Results:

- Number of votes cast in this election: **369,711**
- Breakdown of number of votes and percentage of total votes for each county in precinct:
    - Jefferson: 38,855 votes (10.5% of total)
    - Denver: 306,055 votes (82.8% of total)
    - Arapahoe: 24,801 votes (6.7% of total)
- Based on results above, Denver county had the largest number of votes.
- Breakdown of number of votes and percentage of total votes for each candidate received:
    - Charles Casper Stockham: 85,213 votes (23.0% of total)
    - Diana DeGette: 272,892 votes (73.8% of total)
    - Raymon Anthony Doane: 11,606 votes (3.1% of total)
- Diana DeGette won the election. Her results are shown below:
    - Vote count: 272,892
    - Percentage of total votes: 73.8%

The results above have been printed to a text file, but a screenshot of the Python terminal output has been pasted below for confirmation:

![Terminal_Output](https://github.com/bfox87/Election_Analysis/blob/main/analysis/Terminal_Output.PNG)

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

## Election Audit Summary

This Python script has resulted in a accurate, efficient audit of this precinct's congressional election results. However, the real benefit will come from its use in future elections. The script can be modified to summarize results in a variety of different ways, as detailed below.

### Potential future uses of this Python script:

- Different geographical breakdowns:
    - Depending on the size and type of election, the breakdown of votes by different geographical regions can be achieved. District or precinct level data for state-wide elections. zip codes? 

- Demographics analysis of voter registration
- Types of votes used (mail-in ballots, punch cards, direct recording electronic (DRE counting machines)
- Need to create variables, for loop and then print them
