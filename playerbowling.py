from random import randint,choice
from utils import *

def select_bowler(available_bowlers):
    """Select a bowler  from the available bowlers"""
    print("Available bowlers:", ', '.join(available_bowlers))
    bowler = input("Enter the bowler you want to choose: ").strip().lower()
    while bowler not in available_bowlers:
        print("Enter a valid bowler")
        print("Available bowlers:", ', '.join(available_bowlers))
        bowler = input("Enter the bowler you want to choose: ").strip().lower()
    return bowler


def pbowl(bat, bowl,score=None):
    inning1dict = {"score": 0, "wickets": 0}
    batorder = {}
    bowlerstats = {}

    onstrike = bat[0]
    bat.remove(onstrike)


    offstrike = bat[1]
    bat.remove(offstrike)
 
    batorder[onstrike] = {"balls":0, "runs":0}
    batorder[offstrike] = {"balls":0, "runs":0}
    
    
    over = 0
    balls = 0
    prevbowler = "" 

    while over < 5:
        bowler = select_bowler(bowl)
        bowl.remove(bowler)
        print(f"  Bowler: {bowler} bowling the over")
        #inning1dict["bowler"] = bowler
        if bowler not in bowlerstats.keys():
            bowlerstats[bowler] = {"runs":0, "wickets":0}
        #bowl.remove(bowler)
        if over != 0:

            onstrike,offstrike = offstrike,onstrike
        

        count = 0

        while count < 6:
            print(f"\nScore: {inning1dict['score']}/{inning1dict['wickets']}")
            print(f"Facing batsman: {onstrike}")
            player1 = player_input()
            if score is not None and balls != 60:
                required_rate = (score - inning1dict["score"])//(30-balls)
                #print(f"required rate: {required_rate}")
                comp1 =  randint(4, 6) if required_rate >=4 else randint(1, 6)
                
            else:comp1 =  randint(1, 6)
            count += 1
            balls += 1
            print(f"computer choice :{comp1}")  
            if int(player1) == comp1:
                print("wicket") 
                inning1dict["wickets"] = inning1dict["wickets"]+1
                batorder[onstrike]["balls"] = batorder[onstrike]["balls"]+1
                if inning1dict["wickets"] == 10:
                    print("innings over")
                    display_stats(batorder,bowlerstats)
                    return inning1dict
                onstrike = bat[0]
                bat.remove(onstrike)  
                batorder[onstrike] = {"balls":0, "runs":0}
                bowlerstats[bowler]["wickets"]= bowlerstats[bowler]["wickets"]+1
                #print(bowlerstats)
                
            else:
                runs = comp1
                inning1dict["score"] += runs
                batorder[onstrike]["balls"] += 1
                batorder[onstrike]["runs"] += runs
                bowlerstats[bowler]["runs"] += runs
                if runs in [1,3,5]:
                    onstrike, offstrike = offstrike, onstrike
                print("  scored", comp1)

                
                    #print(batorder)
            if score is not None and inning1dict.get("score",0) > score:   
                print("target achieved" ) 
                display_stats(batorder,bowlerstats)
                return inning1dict     

        over+=1
        display_stats(batorder,bowlerstats)

    return inning1dict    