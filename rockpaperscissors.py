import random
#instructions for game
def instructions():
    """
    print the instructions to the game
    """
    
    print("Instructions:")
    print("Rock, paper, scissors is a game that gives the user 3 options: Rock, paper, or scissors.")
    print("Rock beats scissors, paper beats rock, and scissors beats paper. Same choice ends in a tie.")
    print('The ascii art of "The Rock" represents rock, the ascii art of scissors represents scissors, and the ascii art of a one dollar bill represents paper.')
    print()
    print("***********************************************************************************************************")
    print()

#runs the game and menu 
def rpsmain():
    """
    ask the user if they would like to view the instructions to the game 
    user can also quit the game at anytime in the menu
    display the instrcutions or continue
    allow the user to either play the game or quit
    """
    
    game = True
    while game:
        try:
            #ask the user if they want view the instrcutions, contiue, or quit
            view = input("Would you like to view the instrcutions? Type yes to view, no to continue, or anything else to quit.\n").lower()
            if view == "yes":
                print()
                print("***********************************************************************************************************")
                print()
                instructions()
                view = ""
                
                #start game or quit game
                print()
                start = input("Type play to start the game or type anything else to quit.\n").lower()
                if start == "play":
                    rpcgame()
                else:
                    game = False
            elif view == "no":
                print()
                print("***********************************************************************************************************")
                print()
                #start or quit game
                start = input("Type play to start the game or type anything else to quit.\n").lower()
                if start == "play":
                    rpcgame()
                else:
                    game = False
            else:
                break   
        except:
            pass  
        
#draw choices
def draw(c):
  """
  recieve as a parameter the choice to draw: rock, paper, or scissors
  returns the correct ascii art for the choice recieved
  """
  
  if c == "ROCK":
    #prints rock
    return("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """)
  elif c == "PAPER":
    #prints paper
    return("""
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
    """)
#prints scissors
  elif c == "SCISSORS":
    return("""
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
    """)

#function to make the game
def rpcgame():
    """
    gets the computer's choice by randomly choosing rock, paper, or scissors
    gets the user's choice
    continues through the game while running is True
    """
    
    running = True
    nvalid = False
    options = ["ROCK", "PAPER", "SCISSORS"]
    #determine the outcome of the user choice and computer's choice
    def outcome(p, c):
        """
        takes as a parameters the user's choice and computer's choice
        determines the result of the two choices
        """
        if p == c:
            return("Result: Tie!")
        elif ((p == "PAPER" and c == "ROCK") or (p == "ROCK" and c == "SCISSORS") or (p == "SCISSORS" and c == "PAPER")):
            return ("Result: You won!")
        else:
            return("Result: You lost!")
    #loop for when the game is running
    while running:
      #checks if the inputted choice is valid or not
      if not nvalid:
        print()
        print("***********************************************************************************************************")
        print()
        print("Choices: ROCK, PAPER, or SCISSORS")
      else:
        #reprompt the user
        print("Input is not valid: type ROCK, PAPER, or SCISSORS")
        nvalid = False
      #ask the user 
      print("Enter Q to quit the game")
      pchoice = input().upper()
      #computer's pick
      cchoice = random.choice(options)
      if pchoice in options:
        #check who won
        print("Player chose: ", end = "               ")
        print(pchoice + draw(pchoice))
        print("Computer chose: ", end = "             ")
        print(cchoice + draw(cchoice))
        print(outcome(pchoice, cchoice))
      #quits the game is Q is inputted
      elif pchoice == "Q": 
        running = False
      else:
        nvalid = True
      #ask to play again
      if running and not nvalid:
        playagain = input("Type restart to play again or anything to exit\n").lower()
        print()
        running = playagain == "restart"

    print("Game Over!")

#function that runs the game
if "__main__" == __name__:
    rpsmain()
