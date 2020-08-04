import time
import random

items = []
villians = ["El tunche, an evil spirit",
            "a Simpira, a black jaguar with demon horns"]
villian = random.choice(villians)

def retry():
    reintento = input("Play again (Y/N)").lower()
    if reintento== "y":
        print_pause("Restarting...",2)
        game()
    elif reintento== "n":
        print_pause("Thanks for playing! :D",2)
    else:
        print_pause("I don't understand.",2)
        retry()

def villianname():
    if "tunche" in villian:
        return "El tunche"
    elif "Simpira" in villian:
        return "The Simpira"

def fight():
    action = input("What will you do\n"
                   "1. Fight\n"
                   "2. Run away\n").lower()
    if action =="1" or "fight" in action:
        print_pause("You decided to fight him.",2)
        if "golden spear" in items:
            print_pause("You used your Golden spear to fight"" "
                        + villianname() + ".",2)
            print_pause("You pierced him and"" "+ villianname()
                        + " ""ran away.",2)
            print_pause("Then, you crossed the cave without problem.",2)
            print_pause("You FOUND el dorado, now you can pay your taxes.",2)
            print_pause("You win!",2)
            print_pause("Thanks for playing! :D",2)
        else:
            print_pause("But you realised you don't have any weapon.",2)
            print_pause("You tried your best, but you died.",2)
            print_pause("You failed in your mission.",2)
            retry()           
    elif action =="2" or "run away" in action:
        print_pause("You ran as fast as you can!",2)
        print_pause("Hopefully, you escaped.",2)
        print_pause("You returned to the same place.",2)
        stage()
    else:
        print_pause("You are confused, but you have a chance to choose.\n"
                    "(Check your grammar)",2)
        fight()

def print_pause(sentence, num):
    print(sentence)
    time.sleep(num)

def intro():
    print_pause("You are in Peru, in the Amazonas.", 2)
    print_pause("You're looking for a treasure called 'El dorado'.",2)
    print_pause("But you lost yourself in the jungle.",2)
    print_pause("You arrived at a dangerous zone.",2)
    print_pause("There are a two ways, a cave, and an old hut.",2)

def cave():
    print_pause("You entered to the cave.",2)
    print_pause("You heart something.",2)   
    print_pause("It is"" " + villian + ".",2)
    fight()

    

def hut():
    print_pause("You entered to the hut.",2)
    if "golden spear" not in items:
        print_pause("You noticed there is a Golden spear.",2)
        print_pause("You take it.",2)
        items.append("golden spear")
    
    print_pause("There is anything else to do here, you leave the hut.",2)
    stage() 

def stage():
    choose = input("Where will you go\n"
                   "1. The cave\n"
                   "2. The hut\n").lower()
    if choose =="1" or "cave" in choose:
        cave()  
    elif choose =="2" or "hut" in choose:
        hut()
    else:
        print_pause("You are confused, but you have to escape.\n"
                    "(Check your grammar)",2)
        stage()
     

def game():
    intro()
    stage()

game()

    