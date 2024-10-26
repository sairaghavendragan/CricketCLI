from random import randint

def player_input():
    inp =input("Enter from numbers 1,2,3,4,5,6 \n") 
    while inp not in  ['1', '2', '3', '4', '5', '6']:
        print("Enter a valid number")
        inp = input("Enter from numbers 1,2,3,4,5,6 \n")
    return inp    

def toss  (  ):
    #toss = 0
    result = randint(0, 1)
    inp = input("Enter H for Heads and T for Tails\n").strip().upper() 
    #print(inp)
    while inp != "H" and inp != "T":
        inp = input("Enter H for Heads and T for Tails\n").strip().upper()

    if inp == "H" and result == 1:
        print("you won the toss")
        return 1
    elif inp == "T" and result == 0:
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
        res = randint(0, 1)
        if res == 1:
            print("computer chose batting and you should bowl")
            return 0
            
        else:
            print("computer chose bowling and you should bat")
            return 1
            
      
