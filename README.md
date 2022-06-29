# Audit of Colorado Congressional Election Votes

## Election Audit Overview:
### Background:
A U.S. congressional race was just held in Colorado. A Colorado Board of Elections employee named Tom is needing help with creating a vote count report to certify the results. This is normally done in Excel but Tom's manager wants a more automated process using Python.

### Purpose:
The purpose of this election audit analysis is to verify the total votes counted, the breakdown by votes by county, and the breakdown by candidate to verify the winner of the election just held. Provided this Python analysis is successful, this process will also be used to audit other elections.

## Election-Audit Results:

- Number of votes cast in this election: **369,711**
- Breakdown of number of votes and percentage of total votes for each county in precinct:
    - Jefferson: 38,855 votes (10.5% of total)
    - Denver: 306,055 votes (82.8% of total)
    - Arapahoe: 24,801 votes (6.7% of total)
- Based on results above, Denver county had the largest number of votes.
- Breakdown of number of votes and percentage of total votes each candidate received:
    - Charles Casper Stockham: 85,213 votes (23.0% of total)
    - Diana DeGette: 272,892 votes (73.8% of total)
    - Raymon Anthony Doane: 11,606 votes (3.1% of total)
- Diana DeGette won the election. Her results are shown below:
    - Vote count: 272,892
    - Percentage of total votes: 73.8%

The results above have been printed to a text file in the analysis folder, but a screenshot of the Python terminal output has been pasted below for confirmation:

![Terminal_Output](https://github.com/bfox87/Election_Analysis/blob/main/analysis/Terminal_Output.PNG)

## Election Audit Summary

This Python script has resulted in an accurate, efficient audit of this precinct's congressional election results. However, the real benefit will come from its use in future elections. The script can be modified to summarize results in a variety of different ways, as detailed below.

### Potential future uses of this Python script:

- Different geographical breakdowns:
    - Depending on the size or type of election, the breakdown of votes by different geographical regions can be achieved. For example, an analysis of a state senate district results can be analyzed on a precinct level. 

- Voting method breakdowns:
    - This particular election counted votes from mail-in ballots, punch cards, and results from direct record electronic (DRE) counting machines. Votes in other elections would likely also be compiled from a variety of methods. Python can calculate this breakdown, giving the board of elections insight on how constituents are voting and where to make changes to enable greater voter turnout in future elections.

#### Snippets of code needed for future uses:
- In either of these examples, the original Python code can be adjusted. To begin, an analyst will need to initialize an empty list and dictionary to hold the names (i.e. precinct or vote method) and votes cast as values. Example code pasted below is from the county analysis. 
```
# Create a county list and county votes dictionary.
county_options = []
county_votes = {}
```
Then within a for loop, write a script that gets the name from each row. The number within row[1] can change depending on what column the data is found in.
```
    # For each row in the CSV file.
    for row in reader:

        # Extract the county name from each row.
        county_name = row[1]
```
Next, write a script that checks if the name in the row is within the list you created above. If not, add it to the list and begin tracking the vote count. If so (does match), then add a vote to that name. 
```
        # If statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:

            # Add the existing county to the list of counties.
            county_options.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] +=1
```
Finally, create a variable to hold the votes as they are retrived from the dictionary and calculate those votes as a percentage of the total. Should print these to the terminal and a text file as well.
```
    # Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # Retrieve the county vote count.
        votes = county_votes.get(county_name)
        
        # Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

         # Print the county results to the terminal.
        county_results = (f'{county_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(county_results)   

         # Save the county votes to a text file.
        txt_file.write(county_results)        
```
