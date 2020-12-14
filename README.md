# Colorado Election Results Analysis

## Overview of the project 

This is an analysis of the Colorado election results from the Arapahoe, Denver and Jefferson counties for the election commission . The analysis is looking into a number of specific outputs as well as a business proposal for the election commission regarding potentially using this script (with modifications) for any election. The analysis also looks into the data limitations and provides suggestions for potential use of this script outside of the Colorado state. 

![counties](https://github.com/TamaraGR/Election_Analysis/blob/main/counties.jpg)

## Requested Analysis Outputs 

The Colorado election commission has requested the following outputs:

- [ ] How many votes were cast in this congressional election?
- [ ] Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- [ ] Which county had the largest number of votes?
- [ ] Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- [ ] Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

## Analysis Resources 

 - [x] Analysis code can be found here. [PyPoll_Challenge.py](https://github.com/TamaraGR/Election_Analysis/blob/main/Code/PyPoll_Challenge.py)
 - [x] Data source is [election_results.csv] (https://github.com/TamaraGR/Election_Analysis/blob/main/Resources/election_results.csv)
 - [x] Used software: Python 3.7.6, Visual Studio Code.

## Election Audit Results 

*The election analysis results are presented in the below screenshot and the bulletpoints underneath it.*

![election analysis screenshot](https://github.com/TamaraGR/Election_Analysis/blob/main/election%20analysis%20screenshot.jpg)

- [x] The number of total votes cast in this congressional election is 369,711.
- [x] The Jefferson County received 10.5% of the votes (38,855), Denver received 82.8% (306,055) and Arapahoe received 6.7% (24,801). 
- [x] The county with the largest votes turnout is Denver.
- [x] Candidate Charles Casper Stockham received 23.0% of the votes (85,213), Diana DeGette received 73.8% (272,892) and canddiate Raymon Anthony Doane received 3.1% (11,606). 
- [x] Candidate Diana DeGette won the election with 73.8% (272,892). 

## Elections Business Proposition 

One might think that this script is only good for three countries and three candidates and doesn't apply to real life electoral challenges. Even if that was the case (the code working only for three counties), the state of Delaware only had three counties, and we could sell this script to them. However, the way the current script is written, it can work with as many counties and candidates as needed (even with the state of Texas which has over 200 counties), mostly because it has the following lines of code: 

![code_snippet1](https://github.com/TamaraGR/Election_Analysis/blob/main/code_snippet1.jpg)

At the same time, the current script doesn't provide us with the analysis regarding each candidate's statistics in each county, and that could be another useful piece of information, if we want to suggest this script for elections elsewhere. In the current data sample we only have three candidates and three counties, but we need to have a script that can calculate such information for various numbers of counties and candidates. To not be repetitive we would need to declare additional variables, write a for loop to get the number of votes per each canddiate per each county, calculate the percentages, print the results and write them into the text file. 

It must also be noted that there are database limitations in this case, and in the future the suggestion is to add to the database more details, such as rural/urban population and other demographics. In large cities like, for example, New York, where aside from counties there are also boroughs, a database that relies only on counties' information, will not be sufficient. The last note is that this script and this database account for popular vote only and not for the electoral vote.  
