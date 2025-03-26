from random import randint,choice
from utils import *

def select_batsman(available_batsmen ):
    """Helper function to select and validate the batsman"""  
    print("available batsmen:",', '.join(available_batsmen))
    batsman = input("Enter the batsman's name: ").strip().lower()
    while batsman not in available_batsmen:
        print("Invalid batsman. Please enter a valid batsman.")
        print("available batsmen:",', '.join(available_batsmen))
        batsman = input("Enter the batsman's name: ").strip().lower()
    return batsman





def pbat(bat, bowl,score=None):
    inning1dict = {"score":0, "wickets":0}
     
    batorder = {}
    bowlerstats = {}
    onstrike = select_batsman(bat)
    bat.remove(onstrike)
    offstrike = select_batsman(bat)
    bat.remove(offstrike)
    batorder[onstrike] = {"balls":0, "runs":0}
    batorder[offstrike] = {"balls":0, "runs":0}
    
    
    over = 0
    #balls = 0
    prevbowler = "" 

    while over < 5:
        bowler = choice(bowl[-5:] )
        #inning1dict["bowler"] = bowler
        if bowler not in bowlerstats.keys():
            bowlerstats[bowler] = {"runs":0, "wickets":0}
        bowl.remove(bowler)
        if over != 0:

            onstrike,offstrike = offstrike,onstrike
        print(f"  Bowler: {bowler} bowling the over")

        count = 0
        over_runs = 0
        avgrun = 0


        while count < 6:
            print(f"\nScore: {inning1dict['score']}/{inning1dict['wickets']}")
            print(f"Current batsman: {onstrike}")
            player1 = player_input()
            #avgrun = 0
            avgrun = over_runs//count if count > 0 else 0
            comp1 = randint(4, 6) if avgrun >=4 else randint(1, 6)

            print("Bowler bowls: ", comp1)
            count += 1
            #balls += 1
             
            if int(player1) == comp1:
                print("wicket") 
                inning1dict["wickets"] = inning1dict ["wickets"]+ 1
                batorder[onstrike]["balls"] = batorder[onstrike]["balls"] +1
                if inning1dict["wickets"] == 10:
                    print("innings over")
                    display_stats(batorder,bowlerstats)
                    
                    return inning1dict

                onstrike = select_batsman(bat)
                bat.remove(onstrike)  
                batorder[onstrike] = {"balls":0, "runs":0}
                bowlerstats[bowler]["wickets"]= bowlerstats[bowler]["wickets"]+1
                #print(bowlerstats)
                
            else:
                runs = int(player1)
                inning1dict["score"] += runs
                batorder[onstrike]["balls"] += 1
                batorder[onstrike]["runs"] += runs
                bowlerstats[bowler]["runs"] += runs
                over_runs += runs
                if runs in [1, 3, 5]:
                    onstrike, offstrike = offstrike, onstrike
                print("you have scored", player1)

                 
                    
            if score is not None and inning1dict["score"] > score:  
                print("\nTarget achieved!")
                display_stats(batorder, bowlerstats)
                return inning1dict
        over+=1
        display_stats(batorder, bowlerstats)

    return inning1dict    