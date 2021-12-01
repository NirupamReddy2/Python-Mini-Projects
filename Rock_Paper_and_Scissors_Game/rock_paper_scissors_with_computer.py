import getpass
import sys
import random
#Let's create a rock, paper, scissors game
def another_chance():
    print("As the previous game was a TIE, let's play the game once again")

    player1 = getpass.getpass("what's your choice player1: ")
    print("Please wait computer is choosing")
    computer = random.randint(1, 3)
    #1->ROCK(R), 2->SCISSORS(S), 3->PAPER(P)
    if computer == 1:
        computer = 'R'
    elif computer == 2:
        computer = 'S'
    elif computer == 3:
        computer = 'P'
    #----------------------------------------------------------------------------------------------------------
    if player1 == 'P':
        if computer == 'R':
            print("Yaay! player1 is the winner as he has chosen PAPER and computer has chosen ROCK")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif computer == 'S':
            print("Yaay! computer is the winner as he has chosen SCISSORS and player1 has chosen PAPER")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif computer == 'P':
            print("Oh No! Its a TIE as player1 and computer have chosen PAPER")
            another_chance()
            sys.exit()

    if player1 == 'S':
        if computer == 'R':
            print("Yaay! computer is the winner as he has chosen ROCK and player1 has chosen SCISSORS")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif computer == 'P':
            print("Yaay! player1 is the winner as he has chosen SCISSORS and computer has chosen PAPER")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif computer == 'S':
            print("Oh No! Its a TIE as player1 and computer have chosen SCISSORS")
            another_chance()
            sys.exit()


    if player1 == 'R':
        if computer == 'S':
            print("Yaay! player1 is the winner as he has chosen ROCK and computer has chosen SCISSORS")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif computer == 'P':
            print("Yaay! computer is the winner as he has chosen PAPER and player1 has chosen ROCK")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif computer == 'R':
            print("Oh No! Its a TIE as player1 and computer have chosen ROCK")
            another_chance()
            sys.exit()
#-----------------------------------------------------------------------------------------------------

print("Assume, ROCK as 'R', SCISSORS as 'S', PAPER as 'P'")
print("Select your choice accordingly and enjoy the game. All the best!")

player1 = getpass.getpass("what's your choice player1: ")
print("Please wait computer is choosing")
computer = random.randint(1, 3)
#1->ROCK(R), 2->SCISSORS(S), 3->PAPER(P)
if computer == 1:
    computer = 'R'
elif computer == 2:
    computer = 'S'
elif computer == 3:
    computer = 'P'
#------------------------------------------------------------------------------------------------------------------
if player1 == 'P':
    if computer == 'R':
        print("Yaay! player1 is the winner as he has chosen PAPER and computer has chosen ROCK")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif computer == 'S':
        print("Yaay! computer is the winner as he has chosen SCISSORS and player1 has chosen PAPER")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif computer == 'P':
        print("Oh No! Its a TIE as player1 and computer have chosen PAPER")
        another_chance()
        sys.exit()

if player1 == 'S':
    if computer == 'R':
        print("Yaay! computer is the winner as he has chosen ROCK and player1 has chosen SCISSORS")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif computer == 'P':
        print("Yaay! player1 is the winner as he has chosen SCISSORS and computer has chosen PAPER")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif computer == 'S':
        print("Oh No! Its a TIE as player1 and computer have chosen SCISSORS")
        another_chance()
        sys.exit()


if player1 == 'R':
    if computer == 'S':
        print("Yaay! player1 is the winner as he has chosen ROCK and computer has chosen SCISSORS")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif computer == 'P':
        print("Yaay! computer is the winner as he has chosen PAPER and player1 has chosen ROCK")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif computer == 'R':
        print("Oh No! Its a TIE as player1 and computer have chosen ROCK")
        another_chance()
        sys.exit()