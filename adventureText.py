import sys
import time
from threading import Timer
import random
import traceback

class Game:

    def __init__(self):
        self.win = False
        self.room = 1
        self.firstTime = True
        self.playerHealth = 100
        self.minotaurHealth = 100
        self.roomSixTurnCounter = 0



    def exit(self):
        sys.exit("\nExiting.")



    def victory(self):
        print("\nCongratulations, you've beaten the game!\n")


    
    def roomFiveDoor(self):
        print("\n\nThe door suddenly swings open right in front of your eyes.")
        print("Patience is a virtue.")
        print("You exit the room through the now open doorway.")
        time.sleep(3)
        print("\nYou walk into a pitch black room, and suddenly lights turn on and blind you.")
        print("Use \"look\" to observe your surroundings.\n\n>>> ", end="")
        self.room = 6



    def introduction(self):
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                                                                              
,------.                                         ,--.  ,--.                ,------.                                                
|  .---' ,---.  ,---. ,--,--. ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     |  .-.  \ ,--.,--.,--,--,  ,---.  ,---.  ,---. ,--,--,  
|  `--, (  .-' | .--'' ,-.  || .-. || .-. :    '-.  .-'|  .-.  || .-. :    |  |  \  :|  ||  ||      \| .-. || .-. :| .-. ||      \ 
|  `---..-'  `)\ `--.\ '-'  || '-' '\   --.      |  |  |  | |  |\   --.    |  '--'  /'  ''  '|  ||  |' '-' '\   --.' '-' '|  ||  | 
`------'`----'  `---' `--`--'|  |-'  `----'      `--'  `--' `--' `----'    `-------'  `----' `--''--'.`-  /  `----' `---' `--''--' 
                             `--'                                                                    `---'                         
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")
        time.sleep(3)
        self.tutorial()



    def victory(self):
        time.sleep(3)
        print("""\n\n\n\n\n\n\n\n\n\n
                                                                                                           ,---. 
 ,-----.                                       ,--.          ,--.          ,--.  ,--.                      |   | 
'  .--./ ,---. ,--,--,  ,---. ,--.--. ,--,--.,-'  '-.,--.,--.|  | ,--,--.,-'  '-.`--' ,---. ,--,--,  ,---. |  .' 
|  |    | .-. ||      \| .-. ||  .--'' ,-.  |'-.  .-'|  ||  ||  |' ,-.  |'-.  .-',--.| .-. ||      \(  .-' |  |  
'  '--'\' '-' '|  ||  |' '-' '|  |   \ '-'  |  |  |  '  ''  '|  |\ '-'  |  |  |  |  |' '-' '|  ||  |.-'  `)`--'  
 `-----' `---' `--''--'.`-  / `--'    `--`--'  `--'   `----' `--' `--`--'  `--'  `--' `---' `--''--'`----' .--.  
                       `---'                                                                               '--'  

                                                   ,---. 
,--.   ,--.                 ,--.   ,--.,--.        |   | 
 \  `.'  /,---. ,--.,--.    |  |   |  |`--',--,--, |  .' 
  '.    /| .-. ||  ||  |    |  |.'.|  |,--.|      \|  |  
    |  | ' '-' ''  ''  '    |   ,'.   ||  ||  ||  |`--'  
    `--'  `---'  `----'     '--'   '--'`--'`--''--'.--.  
                                                   '--'  
\n\n\n\n\n\n\n\n\n\n""")



    def tutorial(self):
        print("Welcome to Escape the Dungeon, dear hero! As the title suggests, escape the dungeon to win the game!")
        time.sleep(3)
        print("\nTo move or perform actions, type your action when the prompt ( >>> ) appears.")
        time.sleep(1.5)
        print("Try it now! Type \"help\" then press enter to view the help menu.")
        time.sleep(1.5)
        print("Or type \"skip\" if you already know how to play.")
        time.sleep(1.5)
        print("Type \"skip2\" to skip to the minotaur. Only select this option if you have already played up to the minotaur room.")
        print("This option exists to let you skip \"that\" door. You know what I'm talking about.")
        time.sleep(1.5)
        val = ""
        while val != "help" and val != "skip" and val != "skip2":
            val = input("\n>>> ").replace(" ", "").lower()
            if val == "help":
                self.help()
            elif val == "exit":
                self.exit()
            elif val == "skip":
                break
            elif val == "skip2":
                self.room = 6
                break
            else:
                print("\nPlease type \"help\" to view the help screen, \"skip\" to skip, or \"exit\" to quit the game.")
        if val == "help":
            time.sleep(3)



    def help(self):
        print("\n\n\nTo move or perform actions, type your action when the prompt ( >>> ) appears.")
        print("\nUse WASD to move. For example, type \"w\" then press enter to move forwards.")
        print("\"s\" moves backwards, and \"a\" and \"d\" move left and right.")
        print("\nYou can refer back to this help menu any time by using \"help\".")
        print("\nView your surroundings by using \"look\".")
        print("\nQuit the game with \"exit\".\n\n")


    
    def look(self):
        if self.room == 1:
            print("\nYou find yourself in a dungeon.")
            print("You are in a dark, straight hallway with walls on either side.")
            print("There is a light coming from a door at the end of the hallway.")
        elif self.room == 2 or self.room == 3:
            print("\nYou are in a dark, straight hallway with walls on either side.")
            print("There is a light coming from a door at the end of the hallway.")
        elif self.room == 4:
            print("\nYou find yourself in a well lit room, with a large window on the front wall.")
            print("There are doors to your left and right.")
        elif self.room == 5:
            print("\nYou are in a bare room.")
            print("The only thing here is a locked door in front of you, and a button on the wall next to the door.")
            print("There is a sticky note on the wall next to the button. It reads: \"do not press\".")
            print("Use \"press\" to press the button.")
        elif self.room == 6:
            print("\nYou find yourself in a... wrestling ring?")
            print("There is a closed door in front of you. Wait a second...")
            print("There is a fierce minotaur here! The minotaur is attacking!")
            print("You draw your trusty \"Hero's Blade\" and \"Protagonist's Plot Armor Shield\". To arms!")
            print("Use \"attack\" to attack the minotaur, or \"block\" to block a possible attack from the minotaur.")
        elif self.room == 7:
            print("\nYou are in yet another room.")
            print("There is a closed door in front of you. Wait a second...")
            print("There is an olympic pool here blocking your path to the door, but it's split in half.")
            print("The left half of the swimming pool contains crystal clear water.")
            print("The right half of the swimming pool contains a suspicious, bubbling, purple liquid.")
            print("Use \"left\" to swim through the left side of the swimming pool.")
            print("Use \"right\" to swim through the right side of the swimming pool.")
        elif self.room == 8:
            possibilities1 = ["dark", "bright", "stone", "wooden", "short", "long", "very long", "ridiculously long"]
            possibilities2 = ["faint", "bright", "blinding", "dim", "warm", "cool", "red", "blue", "green",]
            print("\nYou are in a " + random.choice(possibilities1) + ", straight hallway with walls on either side.")
            print("There is a " + random.choice(possibilities2) + " light coming from a door at the end of the hallway.")



    def play(self):
        self.introduction()
        val = ""
        while self.win == False:
            if self.firstTime == True:
                self.look()
            if self.room == 5:
                timeout = 45 # in seconds
                timer = Timer(timeout, self.roomFiveDoor)
                timer.start()
                val = input("\n>>> ").replace(" ", "").lower()
                timer.cancel()
            else:
                val = input("\n>>> ").replace(" ", "").lower()
            self.roomHelper(val)

        self.victory()



    def roomHelper(self, val):
        if self.room == 1:
            self.firstTime = False
            if val == "exit":
                self.exit()
            elif val == "help":
                self.help()
            elif val == "look":
                self.look()
            elif val == "w":
                self.room += 1
                self.firstTime = True
            elif val == "a" or val == "s" or val == "d":
                print("\nYou can't go that way.")
            else:
                print("\nInvalid action.")
        elif self.room == 2 or self.room == 3:
            self.firstTime = False
            if val == "exit":
                self.exit()
            elif val == "help":
                self.help()
            elif val == "look":
                self.look()
            elif val == "w":
                self.room += 1
                self.firstTime = True
            elif val == "s":
                self.room -= 1
                self.firstTime = True
            elif val == "a" or val == "d":
                print("\nYou can't go that way.")
            else:
                print("\nInvalid action.")
        elif self.room == 4:
            self.firstTime = False
            if val == "exit":
                self.exit()
            elif val == "help":
                self.help()
            elif val == "look":
                self.look()
            elif val == "w":
                print("\nYou can't go that way.")
            elif val == "s":
                self.room += 1
                self.firstTime = True
            elif val == "a" or val == "d":
                self.room = 4
                self.firstTime = True
            else:
                print("\nInvalid action.")
        elif self.room == 5:
            self.firstTime = False
            if val == "exit":
                self.exit()
            elif val == "help":
                print("\n\n\nTo move or perform actions, type your action when the prompt ( >>> ) appears.")
                print("\nUse WASD to move. For example, type \"w\" then press enter to move forwards.")
                print("\"s\" moves backwards, and \"a\" and \"d\" move left and right.")
                print("\nYou can refer back to this help menu any time by using \"help\".")
                print("\nView your surroundings by using \"look\".")
                print("\nQuit the game with \"exit\".")
                print("\nPatience is a virtue.\n\n")
            elif val == "look":
                self.look()
            elif val == "w":
                print("\nThe door is locked.")
            elif val == "s" or val == "a" or val == "d":
                print("\nYou can't go that way.")
            elif val == "press":
                possibilities = ["Nothing happens.", "Did something happen?", "You swear you hear a sound.", "Dead silence."]
                print("\nYou press the button. " + random.choice(possibilities))
            else:
                print("\nInvalid action.")
        elif self.room == 6:
            self.firstTime = False
            if val == "exit":
                self.exit()
            elif val == "help":
                self.help()
            elif val == "look":
                self.look()
            elif val == "w":
                print("\nYou can't just walk past the minotaur!")
            elif val == "s":
                print("\nYou can't just flee from the minotaur!")
            elif val == "a" or val == "d":
                print("\nYou can't go that way.")
            elif val == "attack":
                yourDamage = random.randint(1, 19)
                print("\nYou attacked with your sword and dealt " + str(yourDamage) + " damage to the minotaur!")
                self.minotaurHealth -= yourDamage
                print("The minotaur has " + str(self.minotaurHealth) + "/100 health remaining.")
                time.sleep(1)
                minotaurDamage = random.randint(15, 19)
                print("\nThe minotaur dealt " + str(minotaurDamage) + " damage to you!")
                self.playerHealth -= minotaurDamage
                print("You have " + str(self.playerHealth) + "/100 health remaining.")
                self.roomSixTurnCounter += 1
                time.sleep(1)
                if self.roomSixTurnCounter >= 5:
                    print("\nWith one final burst of power, the minotaur attacks you suddenly, catching you off guard.")
                    print("You were no match for the minotaur.")
                    sys.exit("\nGame Over")
            elif val == "block":
                print("\nThe minotaur attacked you, but you blocked the attack with your shield!")
                print("The minotaur has " + str(self.minotaurHealth) + "/100 health remaining.")
                print("You have " + str(self.playerHealth) + "/100 health remaining.")
                self.roomSixTurnCounter += 1
                if self.roomSixTurnCounter >= 5:
                    time.sleep(1)
                    if self.minotaurHealth == 100:
                        print("\nThe minotaur stops attacking you. He looks happy that you didn't want to harm him.")
                        print("He opens the door at the front of the room for you and gestures for you to go through.")
                        print("You smile to the minotaur and enter the next room.")
                        print("It's a good thing that you're a kind soul, and didn't try to hurt the minotaur in any previous playthroughs of this game... right?")
                        self.room += 1
                        self.firstTime = True
                        time.sleep(3)
                    else:
                        print("\nWith one final burst of power, the minotaur attacks you suddenly, catching you off guard.")
                        print("You were no match for the minotaur.")
                        time.sleep(2)
                        sys.exit("\nGame Over")
            else:
                print("\nInvalid action.")
        elif self.room == 7:
            self.firstTime = False
            if val == "exit":
                self.exit()
            elif val == "help":
                self.help()
            elif val == "look":
                self.look()
            elif val == "w":
                print("\nYou must swim across.")
            elif val == "s" or val == "a" or val == "d":
                print("\nYou can't go that way.")
            elif val == "left":
                print("\nThe crystal clear water was actually crystal clear acid. Yikes!")
                time.sleep(2)
                sys.exit("\nGame Over")
            elif val == "right":
                print("\nThe suspicious purple fluid was actually just a lot of spilled grape soda!")
                print("You swim to the other side sweet and sticky, but unharmed.")
                self.room += 1
                self.firstTime = True
                time.sleep(3)
            else:
                print("\nInvalid action.")
        elif self.room == 8:
            self.firstTime = False
            if val == "exit":
                self.exit()
            elif val == "help":
                self.help()
            elif val == "look":
                self.look()
            elif val == "w" or val == "s":
                self.room = 8
                self.firstTime = True
            elif val == "a" or val == "d":
                print("\nThe walls are not as solid as they seem!")
                time.sleep(1)
                print("You push the wall, revealing a secret door leading to a staircase upwards.")
                time.sleep(1)
                print("Upon climbing all the stairs, you find yourself outside.")
                time.sleep(1)
                print("You have escaped the dungeon!")
                self.win = True
            else:
                print("\nInvalid action.")

# --------------------------------------------------------------------------------------------------------------------

def main():
    try:
        game = Game()
        game.play()
    except SystemExit:
        raise
    except:
        print("")
        traceback.print_exc()
        sys.exit("\nOops, something bad happened... Tell Cameron he screwed up his program.")

if __name__ == "__main__":
    main()