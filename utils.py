from random import randint
import time

def player_input():
    inp =input("Enter from numbers 1,2,3,4,5,6 \n") 
    while inp not in  ['1', '2', '3', '4', '5', '6']:
        print("Enter a valid number")
        inp = input("Enter from numbers 1,2,3,4,5,6 \n")
    return inp    

def toss  (  ):
    """Simulate the cricket toss"""#toss = 0
    result = randint(0, 1)
    inp = input("Enter H for Heads and T for Tails\n").strip().upper() 
    print(inp)
    while inp != "H" and inp != "T":
        print("Invalid choice. Please enter H or T.")
        inp = input("Enter H for Heads and T for Tails\n").strip().upper()
    print("\nTossing the coin...")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")    
    toss_result = "Heads" if result == 1 else "Tails"
    print(f"The coin shows: {toss_result}")
    if (inp == "H" and result == 1) or (inp == "T" and result == 0):
        print("you won the toss")
        return 1
     
    else :
        print("you lost the toss")  
        return 0  
    

def choose_bat_or_bowl(toss):

    if toss == 1:
        inp = input("Enter B for Batting and W for Bowling\n").strip().upper()

        while inp != "B" and inp != "W":
            inp = input("Enter B for Batting and W for Bowling\n").strip().upper()

        if inp == "B":
            print("you chose batting")
            return 1
           

        elif inp == "W":
            print("you chose bowling")
            return 0
            
    else:
        print("computer won the toss and deciding...")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")
        res = randint(0, 1)
        if res == 1:
            print("computer chose batting and you should bowl")
            return 0
            
        else:
            print("computer chose bowling and you should bat")
            return 1
            
      
def display_stats (batorder,bowlerstats):
    """Helper function to display the batting and bowling statistics"""
    print("Batting Statistics:")
    for batsman, stats in batorder.items():  
        print(f"{batsman}: {stats['runs']}({stats['balls']} ) ")  

    print("\nBowling Statistics:") 
    for bowler, stats in bowlerstats.items():
        print(f"{bowler}: {stats['wickets']}/({stats['runs']} ) ")
