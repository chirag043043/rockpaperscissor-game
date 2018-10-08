import random

options = ['Rock','Paper','Scissor']
computer =options[random.randint(0,2)]
player = 'false';
while player !='exit':
    player = input("Rock, Paper, Scissor?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        print("Rock not rock or ROCK")
    player = 'False'
    computer = options[random.randint(0,2)]
    print("type exit to leave")
    player = input()

