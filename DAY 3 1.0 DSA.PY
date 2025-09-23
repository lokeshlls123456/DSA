total_friends = int(input())
num_teams = int(input())

friends_per_team = total_friends // num_teams
left_out = total_friends % num_teams

# Displaying the result
print(f"The number of friends in each team is {friends_per_team} and left out is {left_out}")