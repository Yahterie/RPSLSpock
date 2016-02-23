from game import playerChoice, PcChoice

if playerChoice == "PAPER" or PcChoice == "PAPER":
    "PAPER" > "ROCK"
    "PAPER" > "SPOCK"

if playerChoice == "ROCK" or PcChoice == "ROCK":
    "ROCK" > "LIZARD"
    "ROCK" > "SCISSORS"

if playerChoice == "LIZARD" or PcChoice == "LIZARD":
    "LIZARD" > "SPOCK"
    "LIZARD" > "PAPER"

if playerChoice == "SPOCK" or PcChoice == "SPOCK":
    "SPOCK" > "SCISSORS"
    "SPOCK" > "ROCK"

if playerChoice == "SCISSORS" or PcChoice == "SCISSORS":
    "SCISSORS" > "PAPER"
    "SCISSORS" > "LIZARD"
    

if PcChoice == "PAPER":
    "PAPER" > "ROCK"
    "PAPER" > "SPOCK"

if PcChoice == "ROCK":
    "ROCK" > "LIZARD"
    "ROCK" > "SCISSORS"

if PcChoice == "LIZARD":
    "LIZARD" > "SPOCK"
    "LIZARD" > "PAPER"

if PcChoice == "SPOCK":
    "SPOCK" > "SCISSORS"
    "SPOCK" > "ROCK"

if PcChoice == "SCISSORS":
    "SCISSORS" > "PAPER"
    "SCISSORS" > "LIZARD"