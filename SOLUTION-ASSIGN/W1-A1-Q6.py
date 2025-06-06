"""
Ask number of games played in a tournament. 
Ask the user number of games won and number of games loss. 
Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)
"""

no_of_games = int(input("enter the no of games played: "))
game_won=int(input("enter the games won: "))
game_lost=int(input("enter the games lost: "))

tie= no_of_games - game_won - game_lost
total_point=game_won*4+tie*2
print(f"No of game tied : {tie}")
print(f"total points gained : {total_point}")
