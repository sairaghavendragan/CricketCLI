from random import randint,choice
from playerbatting import *
from playerbowling import *

teams = {}
inning1dict = { }
#teams = ["India", "Australia", "Sri Lanka", "New Zealand", "England"]
teams['IND'] =  ["rohit", "shikhar", "kohli", "raina", "pant","pandya","dhoni","bhuvi","kuldeep","chahal","bumrah"]
teams['AUS'] =  ["watson", "warner", "smith", "marnus", "maxwell","green","carey","starc","cummins","behrendoff","zampa"]
teams['SL'] =  ["dilshan" , "jayasurya", "sangakkara", "mahela", "perera","mathews","chandimal","malinga","muralidharan","mendis","vaas"]
teams['NZ'] =  ["guptill", "latham", "kane", "taylor", "mitchell","rachin","santner","ferguson","neesham","boult","southi"]
teams['ENG'] =  ["roy", "bairstow", "root", "stokes", "morgan","buttler","woakes","archer","sam","anderson","moeen"]




def chooseteams( ):
    Player_team = input("Enter the team you want to play for (IND, AUS, SL, NZ,ENG)\n").strip().upper()
    while Player_team not in ['IND', 'AUS', 'SL', 'NZ', 'ENG']:
        print("Enter a valid team")
        Player_team = input("Enter the team you want to play for (IND, AUS, SL, NZ,ENG)\n").strip().upper()
    #teams.pop(Player_team)
    player = teams[Player_team].copy()
    teams.pop(Player_team)
    comp_team = input("Enter the team you want to play against   " + ', '.join(teams.keys()) + "\n").strip().upper()     
    while comp_team not in teams.keys():
        print("Enter a valid team")
        comp_team = input("Enter the team you want to play against  " + ', '.join(teams.keys()) + "\n").strip().upper()
    comp = teams[comp_team].copy()
    teams.pop(comp_team)    
    return [player, comp]





 


def game():
    active =chooseteams( )
    winner = toss()
    chooser = choose_bat_or_bowl(winner)
    if chooser == 0:
        innings = pbowl(active[1].copy(),  active[0].copy())
        target = innings["score"]
        inningschase = pbat(active[0].copy(), active[1].copy(), target)
    else:    
        innings = pbat(active[0].copy(),  active[1].copy())  
        target = innings["score"]
        inningschase = pbowl(active[1].copy(), active[0].copy(), target) 


    print(innings,inningschase)
     

game()