numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)
babies = ["Aya", "Mia", "Lia", "Nina", "Rauf"]
for i in range(len(babies)):
    print(babies[i])
    len(babies)
counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
      print(counties_tuple[i])
for county in counties_tuple:
      print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county, value in counties_dict.items():
    print(county, value)
  
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for i in range(len(voting_data)):

      print(voting_data[i])
for county in range(len(voting_data)):

     print(county)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:  

     print(county_dict.values())
for county_dict in voting_data:    

   for value in county_dict:      

       print(value)
for county_dict in voting_data:

     print(county_dict['registered_voters'])
for county_dict in voting_data:

     for key, value in county_dict.items():

         print(value)
for county_dict in voting_data:
    print(county_dict['county'])

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
f'{value:{width}.{precision}}'
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
    