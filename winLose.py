from game import playerChoice, PcChoice

if playerChoice > PcChoice:
    print ("{} beats {}!".format(playerChoice, PcChoice))
    print ("Congratulations, you WIN!")
    import again

if playerChoice < PcChoice:
    print ("{} beats {}!".format(PcChoice, playerChoice))
    print ("You LOSE! Better luck next time.")
    import again

if playerChoice == PcChoice:
    print("It's a tie!")
    import again
   