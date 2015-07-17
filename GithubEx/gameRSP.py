
#Rock, Paper, Scissors, Lizard, Spock game

# Import the necessary Libraries
import math
import random


# Function to convert name to number
def name_to_number(name):
    if name.lower() == "rock":
        tempVal = 0
    elif name.lower() == "spock":
        tempVal = 1
    elif name.lower() == "paper":
        tempVal = 2
    elif name.lower() == "lizard":
        tempVal = 3
    elif name.lower() == "scissors":
        tempVal = 4
     
    else:
        print "Invalid Input; please use one of the expected options" + "\n"
        tempVal = -1
     
    return tempVal

# Function to convert number to name
def number_to_name(num):
    if num == 0:
        tempVal = "rock".capitalize()
    elif num == 1:
        tempVal = "spock".capitalize()
    elif num == 2:
        tempVal = "paper".capitalize()
    elif num == 3:
        tempVal = "lizard".capitalize()
    elif num == 4:
        tempVal = "scissors".capitalize()
     
    else:
        print "Invalid Input; Please use a number between 0 and 4, both inclusive"
        tempVal = -1
     
    return tempVal        

# Function to display output of game
def rpsls(player_choice):
    print "Player Chooses " + player_choice
    player_number = name_to_number(player_choice)
    if player_number != -1:
        comp_number = random.randrange(0,5)
        comp_name = number_to_name(comp_number)
        print "Computer chooses " + comp_name
        #Calculate game number
        gameNum = ((comp_number - player_number) % 5)
        print gameOutput(gameNum)+ "\n" 
   
# Function to return, computer or player win! or is it a Tie!!!        
def gameOutput(gameNum):
    if gameNum == 1 or gameNum == 2:
        strOutput = "Computer wins!"
    elif gameNum == 3 or gameNum == 4:
        strOutput = "Player wins!"
    elif gameNum == 0:
        strOutput = "Player and computer tie!"
    return strOutput

   

