import random 

choice = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"] 
##PcChoice = random.choice(choice)
PcChoice = "ROCK"

print ("Let's play a game!")
playerChoice = input("Please type ROCK, PAPER, SCISSORS, LIZARD, or SPOCK.")
    
print("")
print("You chose {}!".format(playerChoice))
print("Computer chose {}!".format(PcChoice))



