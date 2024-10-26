from random import randint,choice
from utils import *

def pbat(bat, bowl,score=None):
    inning1dict = {}

    onstrike = input("Enter from names" + ', '.join(bat)  +   "\n").strip().lower()
    while onstrike not in bat:
        print("Enter a valid name")
        onstrike = input("Enter from names" + ', '.join(bat) + "\n").strip().lower()
    bat.remove(onstrike)


    offstrike = input("Enter from names" + ', '.join(bat)  +   "\n").strip().lower()   
    while offstrike not in bat:
        print("Enter a valid name")
        offstrike = input("Enter from names" + ', '.join(bat)  + "\n").strip().lower()
    bat.remove(offstrike)

    

    #inning1dict["onstrike"] = onstrike
    #inning1dict["offstrike"] = offstrike
    inning1dict["score"] = 0
    inning1dict["wickets"] = 0
    batorder = {}
    bowlerstats = {}
    batorder[onstrike] = {"balls":0, "runs":0}
    batorder[offstrike] = {"balls":0, "runs":0}
    
    
    over = 0
    balls = 0
    prevbowler = "" 

    while over < 5:
        bowler = choice(bowl[-2:] )
        inning1dict["bowler"] = bowler
        if bowler not in bowlerstats.keys():
            bowlerstats[bowler] = {"runs":0, "wickets":0}
        bowl.remove(bowler)
        if over != 0:

            onstrike,offstrike = offstrike,onstrike
        

        count = 0

        while count < 6:
            player1 = player_input()
            comp1 = randint(1, 6) 
            count+=1
            print( comp1)
            if int(player1) == comp1:
                print("wicket") 
                inning1dict["wickets"] = inning1dict.get("wickets",0)+1
                batorder[onstrike]["balls"] = batorder[onstrike].get("balls",0)+1
                if inning1dict["wickets"] == 10:
                    return inning1dict

                onstrike = input("Enter from names" + ', '.join(bat)  +   "\n").strip().lower()
                while onstrike not in bat:
                    print("Enter a valid name")
                    onstrike = input("Enter from names" + ', '.join(bat) + "\n").strip().lower()
                bat.remove(onstrike)  
                batorder[onstrike] = {"balls":0, "runs":0}
                bowlerstats[bowler]["wickets"]= bowlerstats[bowler].get("wickets",0)+1
                print(bowlerstats)
                
            else:
                if player1 in ['1','3','5']:
                    inning1dict["score"] = inning1dict.get("score",0)+ int(player1)
                    batorder[onstrike]["balls"] = batorder[onstrike].get("balls",0)+1
                    batorder[onstrike]["runs"] = batorder[onstrike].get("runs",0)+ int (player1)
                    bowlerstats[bowler]["runs"]= bowlerstats[bowler].get("runs",0) + int(player1)
                    onstrike,offstrike= offstrike,onstrike
                    print("you have scored", player1)

                else:
                    inning1dict["score"] = inning1dict.get("score",0)+ int(player1)
                    batorder[onstrike]["balls"] = batorder[onstrike].get("balls",0)+1
                    batorder[onstrike]["runs"] = batorder[onstrike].get("runs",0)+ int(player1)
                    bowlerstats[bowler]["runs"]= bowlerstats[bowler].get("runs",0) + int(player1)

                    print("you have scored", player1)
                    #print(batorder)
            if score is not None and inning1dict.get("score",0) > score:  
                print("player team won the match") 
                print(batorder)
                print(inning1dict)
                print(bowlerstats)
                return inning1dict    
        over+=1
        print(batorder)
        print(inning1dict)
        print(bowlerstats)

    return inning1dict    