
import random
import time
global Current_Level_XP
global Next_Level_XP

Out_Of_Combat = 1
Health = 100
Gold = 0
Level = 1
Next_Level_XP = 100
Current_Level_XP = 0
x=1

def Coin_Choice():
    #Subroutine which Carries out a coin flipping Choice, either heads or tails to check if it is valid.
    Choice_Made = 1
    while Choice_Made == 1:
        
        #Takes the input and applies to choice variable and makes lowercase.
        Choice = input()
        Choice = Choice.lower()

        #Checks to see if choice is heads or tails. If not then a new answer
        #must be entered.
        if Choice != 'heads' and Choice != 'tails':
                print("Please input either heads or tails.")
        elif Choice == "heads":
            print("You chose heads")
            Choice_Made = 2
        else:
            print("You chose tails")
            Choice_Made = 3

    #Returns the value for Choice_Made
    return Choice_Made
            
def Battle_First_Turn():
    print("")
    print('''A battle is about to start, a coin must be flipped to decide the first turn.
What face of the coin will it land on?''')
    print("")
    #Generates a value as if flipping a coin heads = 2 tails = 3
    Coin_Flip = random.randint(2,3)
    
    #Gathers Choice_Made from Coin_Choice()
    Choice_Made = Coin_Choice()

    #If Coin_Made is the same as the face the appropriate phrase is applied.
    if Choice_Made == 2:
        Face_Win = "Heads!"
        Face_Fail = "Tails"
    else:
        Face_Win = "Tails!"
        Face_Fail = "Heads"

    #If the Choice made is the same as the Face that landed after the coin flip the player gets first turn.
    #Otherwise the enemy gets first turn.
    if Choice_Made == Coin_Flip:
        print("The coin landed on...", end='')
        time.sleep(1)
        print(Face_Win)
        time.sleep(0.5)
        print("")
        print("You get the first turn!")
        First_Turn = 1
    else:
        print("The coin landed on...", end='')
        time.sleep(1)
        print(Face_Fail)
        time.sleep(0.5)
        print("")
        print("The enemy gets the first turn!")
        First_Turn = 0
    return First_Turn
        
def Battle():
    global Health
    global Stamina
    global Kill_timer
    global Enemy_Damage
    Kill_timer = 0
    Health = 100
    Stamina = 200
    Enemy_Health = 100
    Valid_Turn = 0
    
    #Checks if player gets first turn.
    First_Turn = Battle_First_Turn()

#States if health is stil higher than 0 then battle continues. 
    while Enemy_Health > 1 or Health > 1:
        Kill_timer = Kill_timer + 1
        
#If first turn is platyers...
        if First_Turn == 1:
            
#Asks user what he / she wants to do.
            print("")
            print("What would you like to do?")
            print("1.Attack")
            print("2.Run")
            print("3.Skip Turn")
            print("")
            
#Makes sure the data entered is valid.
            while First_Turn == 1:
                Battle_Choice = input()
                if Battle_Choice != "1" and Battle_Choice != "2" and Battle_Choice != "3":
                    print("please input either 1, 2 or 3")
                    Valid_Turn = 0
                    
#Data is valid and will use the 1st option.
#Sets an amount to hit enemy and takes damage off.
#If the damage is above 15 a critical hit message will appear.
                elif Battle_Choice == "1":
                    print("")
                    print("Which attack do you want to use?")
                    print("1.Basic : One hit taking 20 stamina")
                    print("2.Flurry : Three Consecutive hits taking 150 Stamina")
                    Attack_Choice = input()
                    if Attack_Choice == "1":
                        if Stamina < 20:
                            print("You dont have enough stamina")
                            
                        else:
                            Enemy_Damage = random.randint(1,30)
                            Stamina = Stamina - 20
                            Enemy_Health = Enemy_Health - Enemy_Damage
                            print("")
                            Damage_Calculator()
                            if Enemy_Health < 1:
                                Enemy_Health = 0
                                print("You Won the Battle!")
                                Loot_Generator()
                                return
                            if Stamina < 0:
                                First_Turn = 2
                            First_Turn = 2
                            Valid_Turn = 1
                        
                    elif Attack_Choice == "2":
                        if Stamina < 150:
                            print("You dont have enough stamina")
                            
                        else:
                            Enemy_Damage = random.randint(1,30)
                            Enemy_Health = Enemy_Health - Enemy_Damage
                            time.sleep(0.5)
                            Damage_Calculator()

                            Enemy_Damage = random.randint(1,20)
                            Enemy_Health = Enemy_Health - Enemy_Damage
                            time.sleep(0.5)
                            Damage_Calculator()
                        
                            Enemy_Damage = random.randint(1,30)
                            Enemy_Health = Enemy_Health - Enemy_Damage
                            time.sleep(0.5)
                            Damage_Calculator()
                        
                            Stamina = Stamina - 150
                    
                            if Enemy_Health < 1:
                                Enemy_Health = 0
                                print("You Won the Battle!")
                                Loot_Generator()
                                return
                            First_Turn = 2
                            Valid_Turn = 1
                            
                    elif Attack_Choice != "1" or Attack_Choice != "1":
                        print("Please select a skill with either 1 or 2")
                
                        
                elif Battle_Choice == "2":
                    Run_Chance = random.randint(1,100)
                    if Run_Chance < 30:
                        print("You managed to escape")
                        return
                    else:
                        Trip_Loss = random.randint(1,10)
                        print("You fell and lost ", Trip_Loss, " Health! and continued to battle.")
                        Health = Health - Trip_Loss
                        First_Turn = 2

                    Valid_Turn = 1

                elif Battle_Choice == "3":
                    print("")
                    print("You skip your turn")
                    print("")
                    First_Turn = 2

        
#Enemy attack
        else:
            print("")
            Enemy_Hit = random.randint(0,20)
            print("The enemy attacks hitting ",Enemy_Hit , "!", end = "")
            Health = Health - Enemy_Hit
            Stamina = Stamina + random.randint(1,10)
            if Enemy_Hit > 15:
                print("CRITICAL HIT!")
                print("")
            print("")
            if Health < 1:
                Health = 0
                print("You have died...")
                return 
            else:
                First_Turn = 1
            time.sleep(1)
            Valid_Turn = 1

            if Stamina > 200:
                Stamina = 200
            
                
#Displays player and enemy health and player stamina after every move.                
        if Valid_Turn == 1:
            print(" ")
            print("")
            print("Your Health : ", Health, "/ 100")
            print("Your Stamina : ", Stamina, "/ 200")
            print("Enemy Health :", Enemy_Health, "/ 100")
            print("")
            
def Damage_Calculator():
    print("You attack hitting ", Enemy_Damage, "!", end = '')
    if Enemy_Damage > 15:
        print(" CRITICAL HIT!")
        print("")
        time.sleep(1)
        Valid_Turn = 1
    else:
        print("")
        print("")

#Generates loot and xp depending on player performance.
def Loot_Generator():
    global Gold_Gained
    global Gold
    Gold_Gained = 1000 // Kill_timer
    print("You have gained ", Gold_Gained, " gold.")
    Gold = Gold + Gold_Gained
    Loot = ["Sword of awesome", "Health potion x 2", "Nothing"]
    Loot_Randomiser = random.randint(0,2)
    print("Loot: ", Loot[Loot_Randomiser])

def XP_Generator():
    global Current_Level_XP
    global Level
    global Next_Level_XP
    
    Current_Level_XP = Current_Level_XP + (10 * Kill_timer)

    if Current_Level_XP >= Next_Level_XP:
        Previous_Level_XP = Current_Level_XP
        Next_Level_XP = (Previous_Level_XP)*5
        Level = Level + 1
    return


print("To use this game, type any of these commands")
print("")
print("Fight: Starts a battle!")
print("Info: Shows player information (Only out of battle)")
print("")
    
while Out_Of_Combat == 1:
    O_of_C_Command = input().lower()
    x = x + 1
    
#Starts a fight
    if O_of_C_Command =='fight':
        Battle()
        if Health > 0:
            XP_Generator()
        print("")
        Out_Of_Combat = 1

        
    elif O_of_C_Command == "info":
        print("Health: ", Health)
        print("Gold: ", Gold,"      Level:", Level, "      XP: ", Current_Level_XP , " / ", Next_Level_XP)
        

    elif O_of_C_Command == "secret":
        print("I", end="")
        time.sleep(0.1)
        print(" a", end="")
        time.sleep(0.1)
        print("m ", end="")
        time.sleep(0.1)
        print("A", end="")
        time.sleep(0.1)
        print("W", end="")
        time.sleep(0.1)
        print("E", end="")
        time.sleep(0.1)
        print("S", end="")
        time.sleep(0.1)
        print("O", end="")
        time.sleep(0.1)
        print("M", end="")
        time.sleep(0.1)
        print("E", end="")
        time.sleep(0.1)
        print("!")
        time.sleep(0.1)

    elif O_of_C_Command == "regen health":
        Health = Health + 100
        if Health > 100:
            Health = 100
        print(" Your Health is now ", Health)
