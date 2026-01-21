#Manjot_Gainda_The_Abandoned_School
#January 19th, 2026
#This is a text based game which provides the user with choices in a story where
#they can create their own adventure, including weapons and bossfights and utilizing
#dictionaries and loops to create an entertaining story

Weapons = {"Water Bottle":{      #The dictionary thst holds all weapons, gets added to and removed from throughout the game
                    "Damage" : 5 #The Damage outpout of a specific weapon
                    },
           }

def fight():
    """This funciton only gets called when the user choose to engage in a fight with an enemy
    It prints all available weapons and their damage output and lets the user choose which one
    They would like to use"""
    
    global health           #This global variable is how much health the current boss has
    global invalid          #This variable tells the function if the choice outputted was invalid
                            #allowing the code to repeatedly call this function until it is no longer
                            #invalid
    global scene_check
    
    invalid = False;        #Invalid starts off as false and only becomes true later

    
    def weapon():
        """This function does the printing of each weapon and lets the user select their
            weapon while also calculating the damage done to the enemy"""
        global health          #brings back the global variables from the fight() function so
        global invalid         #they can be used here

        for weapon in Weapons:  #Cycles through every weapon present in the Weapons dictionary
            data2 = Weapons[weapon]   #sets a variable equal to every individual weapon
            print("\nYou can use", weapon, "for", data2["Damage"])   #prints out all possible weapons you can use
            
        selected_weapon = input("Which weapon would you like to use? ").title()    #Asks the user which weapon they'd like to use
        if selected_weapon in Weapons:    #checks and makes sure the users desired weapon is in the dictionary
            for weapon in Weapons:        #Goes through every weapon until it finds which weapon it is looking for
                if selected_weapon == weapon:      #Finds the weapon the user asked for
                    invalid = False;               #Sets the invalid variable to false just incase the user made it true beforehand
                    data2 = Weapons[weapon]        #Changes the variable to hold the current weapon
                    print("You deal", data2["Damage"], "damage to the enemy!")     #Prints damage output
                    print("\nThe enemy has", health - data2["Damage"], "health left!")      #prints how much health the enemy has
                    health = health - data2 ["Damage"]                  #Changes the enemy's health
                    del Weapons[selected_weapon]                        #deletes the weapon from the inventory
                    break

                    
        else:
            print("INVALID")          #If the user's choice is not in the dictionary, it lets them know it's invallid
            invalid = True;           #changing this variable allows the function to be called again
            
    weapon()                          #Calls the function once when fight() is called
    
    if health != 0 or invalid == True:   #Calls fight() again if the enemy hasn't died or if the user's choice
        fight()                          #is invalid



scenes = {              #This dictionary holds all the scenes in the game
    "start":{           #scene name
        "text" :"Your friend tells you about the 'haunted school'..."       #Text that gets displayed to the user
                "Sheldon Williams. Do you go explore by yourself tonight and prove him wrong? (Yes,No)",
        "choices":{       #Another dicionary that holds the user's possible choices
            "yes": "Outside_School" , "no": "stay",        #Sends the user to a specific scene based on their choice
            }
        },
    "Outside_School":{
    "text" : "You arrive outside the school just as night falls, a twig snaps and you flinch before calming"
            " yourself down. Ghosts aren't real, you'll be just fine! Which entrance do you enter from? (Aud, Window)",
    "choices": {
            "aud": "Aud_Foyer", "window": "Hallway",
            }
        },
    "stay":{
        "text": "You choose to stay home",
        "choices": {}
        },
    "Aud_Foyer":{
        "text": "You enter into the Auditorium Foyer, posters for plays that were produced"
                " by the school long ago scatter the floor... is that.. blood? Do you go"
                " into the Auditorium or down the hallway to your left? (Left, In)",
        "choices": {
            "in": "Aud", "left": "Hallway"
            }
        },
    "Hallway":{
        "text": "You enter the main floor hallway, crumbling and covered in half grown"
                " weeds. You can't believe anybody at any point would choose to come to this school..."
                "Do you go upstairs or downstairs?(up, down)",
        "choices": {
            "up": "Upstairs", "down": "Downstairs"
            }
        },
    "Aud": {
        "text": "You enter the Auditorium. You see the lights flash on and before you even know it,"
                " a creature is charging at you... is that.. Ms. Heuchert? The famous coder? What is she doing here?"
                " It's too late, the creature who has clearly been trapped in the school for far too long grabs a hold"
                "of you and your screams go unheard...",
        "choices": {}
        },
    "Downstairs": {
        "text": "You hear a loud bang coming from the gym... (Explore, Hide)",
        "choices": {
            "explore": "Gym", "hide": "Bathroom"
            }
        },
    "Upstairs":{
        "text": "You enter the old computer lab... wow these computers are aincent! Covered in a thick"
                "layer of dust you're suprised the LED that lets you know they're fully charged is still on."
                " Do you head back downstairs or goof around a little (Goof, Downstairs)",
        "choices": {
            "goof": "Goof", "downstairs": "Downstairs"
            }
        },
    "Gym": {
        "text": "You ran into Zacharias! (fight, run)",
        "choices": {
            "run": "Death", "fight": "fight"
            }
        },
    "fight":{
        "text": " ",
        "choices": {}
        },
    "Bathroom":{
        "text": "You quickly run and hide in a bathroom stall. You're only in there for a few moments but when you open the stall"
                " again you notice you're ontop of a hill. You turn around and the stall is no longer there, you look down and grass"
                " has replaced the bathroom tiles, you look around and see this isn't where you were... or when you were either..."
                " is that a T-Rex over there?",
        "choices":{}
        },
    "Court":{
        "text": "You narrowly take down Zacharias. Walking over his clearly"
                "deformed monstorous body, you get to the basketball court."
                "It's time for a little break after that intense fight,"
                " do you turn the disco lights on or shoot some basketball? (Shoot, Lights)",
        "choices": {
            "shoot": "BBALL", "lights": "Disco"
            }
        },
    "Goof":{
        "text": "You log into some flappy bird but hear a loud CRASH right outside,"
                " the door... Do you keep playing or jump through the open window? (Play, Jump)",
        "choices":{
            "play": "Good_Ending_Comp_Sci", "jump": "Jump"
            }
        },
    "Good_Ending_Comp_Sci":{
        "text": "You ignore the sound and keeo playing... your eyelids grow heavy..."
                "the game begins to flutter in and out of focus... you rest your head and..."
                "fall asleep... Forever.",
        "choices": {}
        },
    "Jump":{
        "text": "You jump out the window but forget you just twisted your ankle! Well... I guess"
                " this is it. SPLAT",
        "choices": {}
        },
    "BBALL":{
        "text": "All of a sudden the ghost of the coach basketball team appears infront of you. He likes what"
                " he sees and wants to 1v1 you. The ball is in your hands... (Shoot, Dunk)",
        "choices":{
            "shoot": "Airball", "dunk": "Good_Ending_Court"
            }
        },
    "Disco":{
        "text": "The lights also turn on the music, blasting music from a time long gone. This summons all the ghosts"
                " to the gym who start breaking it down! Show them that you're just as good of a dancer! (Griddy, Moonwalk)",
        "choices": {
            "griddy": "Item", "moonwalk": "SneakEscape"
            }
        },
    "Airball":{
        "text": "You airball the shot! Your opponent grabs the ball and dunks it on you! Do you keep playing"
                " or run away in embarrassment? (Run, Play)",
        "choices":{
            "run": "Escape", "play": "Death"
            }
        },
    "Good_Ending_Court":{
        "text": "Your viscious dunk shocks the ghost who can't belive the imcomprehensible skill you posses!"
                " You teach the ghost your ways and before you know it you two are best friends and the best"
                " basketball duo in the city!",
        "choices": {}
        },
    "SneakEscape":{
        "text":"You sneakily back out of the gym without anyone noticing, almost like a... smooth criminal"
                " Do you go back in or run away? (Back, Run)",
        "choices":{
            "back": "Dance_Ending", "run": "Disco_Escape_Ending"
            }
        },
    "Item":{
        "text": "The crowd is angered by your move! They claim its too modern and they're getting"
                " rowdy... What do you do now? (Escape, Fight)",
        "choices":{
            "escape": "Escape", "fight": "fight_crowd"
            }
        },
    "fight_crowd":{
        "text": " ",
        "choices":{}
        },
    "Escape":{
        "text": "You run out of the gym to escape! Quick where do you go! (left,right)",
        "choices":{
            "left": "Death", "right": "Panko_fight"
            }
        },
    "Panko_fight":{
        "text": " ",
        "choices":{}
        },
    "Disco_Escape_Ending":{
        "text": "The party rages on behind you as you manage to narrowly escape, but who knows, maybe you'll head"
                " back for one last song someday.",
        "choices":{}
        },
    "Dance_Ending":{
        "text":"You feel bad so you choose to head back instead of abandoning your new friends. You party until the sun comes"
                " up. When you try to see your photos from that night, you notice none of your new ghost friends were captured,"
                " so now it looks like you were dancing alone :(",
        "choices":{}
        },
    "Panko_Escape":{
        "text": "You manage to beat the final boss of Sheldon, Mr. Panko himself. You smile as you limp on out to freedom,"
                " knowing no one will ever believe your story",
        "choices":{}
        },
    "Death": {
        "text": "Unfortunately your escape methods do not work and you end up perishing inside the school...",
        "choices": {}
        }
    }
def play(scene):
    """This function is the most important part of the game. It will check the user's inputted choice
    and send the user to that specific scene as long as it is within the 'choice' dictionary, while also
    handling calling fight() functions, changing health, and providing weapons to the user"""
    global health        #global variable so we can change the health of an enemy as more spawn in
    global scene_check
    while True:
        data = scenes[scene]      #sets a variable equal to a scene within the scenes dicionary
        print("\n"+data["text"])  #prints that specifics scene text out
        if not data["choices"]:
            break
        choice = input("> ").lower()   #takes input from the user on which scene to go to next
        if choice in data["choices"]:  #ensures the choice is valid
            scene = data["choices"][choice]    #changes the current scene to the user selected one
            scene_check = scene
            if scene == "Downstairs":          #checks if the scene is downstairs
                Weapons.update({"Bat": {"Damage": 10}})  #if it is, gives the user a new weapon
                print("\nYou found the Bat Weapon (Damage: 10)!")   #prints out statement about user finding new weapon
            if scene == "Item":                 #checks if the scene is item
                Weapons.update({"Basketball": {"Damage": 10}})     #if it is, gives the user a new weapon
                print("\nYou found the Basketball Weapon (Damage: 10)!")     #prints statement
            if scene == "fight":           #if scene is fight, then the user has selected to engage with an enemy
                health = 15                #sets the boss health to 15
                print ("Zacharias has", health, "health!")   #lets the user know how much health the enemy has
                fight()                 #calls the fight function
                if health <= 0:         #if the enemy is defeated
                    play("Court")       #plays the nect scene
            if scene == "fight_crowd":   #same boss method as the zacharias fight
                health = 10
                print("Fight the crowd!")
                fight()
                if health <= 0:
                    play ("Disco_Escape_Ending")
                    break
            if scene == "Panko_fight":
                health = 10
                print("you ran into PANKO!, he has", health, "health!")
                fight()
                if health <= 0:
                    play ("Panko_Escape")
                    break
        elif choice == "quit":
            exit()
        else:
            print("Invalid choice")
            
     

play("start")


