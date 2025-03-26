from random import randint,choice
from playerbatting import *
from playerbowling import *
import os

class CricketGame:
    """Cricket game class"""
    def __init__(self):
        self.teams = {}
        self.innings1  = None 
        self.innings2  = None
        self.player = {'team': None, 'name': None}
        self.comp = {'team': None, 'name': None}
        #self.target = None
#teams = ["India", "Australia", "Sri Lanka", "New Zealand", "England"]
        self.teams['IND'] =  ["rohit", "shikhar", "kohli", "raina", "pant","pandya","dhoni","bhuvi","kuldeep","chahal","bumrah"]
        self.teams['AUS'] =  ["watson", "warner", "smith", "marnus", "maxwell","green","carey","starc","cummins","behrendoff","zampa"]
        self.teams['SL'] =  ["dilshan" , "jayasurya", "sangakkara", "mahela", "perera","mathews","chandimal","malinga","muralidharan","mendis","vaas"]
        self.teams['NZ'] =  ["guptill", "latham", "kane", "taylor", "mitchell","rachin","santner","ferguson","neesham","boult","southi"]
        self.teams['ENG'] =  ["roy", "bairstow", "root", "stokes", "morgan","buttler","woakes","archer","sam","anderson","moeen"]

    def clear_screen(self):
        """clear screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_title(self):
        """display title"""
        self.clear_screen()
        print("Welcome to the Cricket Game")
        print("---------------------------")

    def chooseteams(self ):
        """choose teams"""
        self.display_title()
        print("Choose your team")
        print("Available teams:", ', '.join(self.teams.keys()) )
        available_teams = self.teams.copy()
        team = input("Enter the team you want to play for (IND, AUS, SL, NZ,ENG)\n").strip().upper()
        while team not in ['IND', 'AUS', 'SL', 'NZ', 'ENG']:
            print("Enter a valid team")
            team= input("Enter the team you want to play for (IND, AUS, SL, NZ,ENG)\n").strip().upper()
        #teams.pop(Player_team)
        self.player['team']  = available_teams[team].copy()
        self.player['name'] = team
        available_teams.pop(team)
        comp_team = input("Enter the team you want to play against   " + ', '.join(available_teams.keys()) + "\n").strip().upper()     
        while comp_team not in available_teams.keys():
            print("Enter a valid team")
            comp_team = input("Enter the team you want to play against  " + ', '.join(available_teams.keys()) + "\n").strip().upper()
        self.comp["team"] = available_teams[comp_team].copy()
        self.comp["name"] = comp_team
        available_teams.pop(comp_team)    
        #return [self.player, comp,Player_team,comp_team]


    def display_match_summary(self,innings1, innings2, team1_name, team2_name ):
        """Display a summary of the match"""
        self.clear_screen()
        print("====================================")
        print("          MATCH SUMMARY            ")
        print("====================================")
        print()
        
        print(f"{team1_name} vs {team2_name}")
        
        print(f"First Innings: {team1_name}")
        print(f"Score: {innings1['score']}/{innings1['wickets']}")
        print()
        
        print(f"Second Innings: {team2_name}")
        print(f"Score: {innings2['score']}/{innings2['wickets']}")
        print()
        
        # Determine the winner
        if innings1['score'] > innings2['score']:
            margin = innings1['score'] - innings2['score']
            winner = team1_name
            print(f"{winner} won by {margin} runs!")
        elif innings2['score'] > innings1['score']:
            wickets = 10 - innings2['wickets']
            winner = team2_name
            print(f"{winner} won by {wickets} wickets!")
        else:
            print("The match ended in a tie!")


 


    def play(self):
        self.chooseteams( )
        winner = toss()
        chooser = choose_bat_or_bowl(winner)
        if chooser == 0:
            self.innings1 = pbowl(self.comp["team"].copy(),self.player["team"].copy())
            target = self.innings1["score"]
            self.innings2 = pbat(self.player["team"].copy(), self.comp["team"].copy(), target)
            self.display_match_summary(self.innings1,self.innings2, self.comp["name"],self.player["name"] )
        else:    
            self.innings1 = pbat(self.player["team"].copy(), self.comp["team"].copy())  
            target = self.innings1["score"]
            self.innings2 = pbowl(self.comp["team"].copy(),self.player["team"].copy(), target) 
            self.display_match_summary(self.innings1,self.innings2, self.player["name"],self.comp["name"] )

    #print(innings,inningschase)
def main():
    game = CricketGame()
    game.play()

if __name__ == "__main__":
    main()
