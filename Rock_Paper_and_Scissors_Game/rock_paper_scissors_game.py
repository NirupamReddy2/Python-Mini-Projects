import getpass
import sys
#Let's create a rock, paper, scissors game
def another_chance():
    print("As the previous game was a TIE, let's play the game once again")

    player1 = getpass.getpass("what's your choice player1: ")
    player2 = getpass.getpass("what's your choice player2: ")

    if player1 == 'P':
        if player2 == 'R':
            print("Yaay! player1 is the winner as he has chosen PAPER and player2 has chosen ROCK")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif player2 == 'S':
            print("Yaay! player2 is the winner as he has chosen SCISSORS and player1 has chosen PAPER")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif player2 == 'P':
            print("Oh No! Its a TIE as player1 and player2 have chosen PAPER")
            another_chance()
            sys.exit()

    if player1 == 'S':
        if player2 == 'R':
            print("Yaay! player2 is the winner as he has chosen ROCK and player1 has chosen SCISSORS")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif player2 == 'P':
            print("Yaay! player1 is the winner as he has chosen SCISSORS and player2 has chosen PAPER")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif player2 == 'S':
            print("Oh No! Its a TIE as player1 and player2 have chosen SCISSORS")
            another_chance()
            sys.exit()


    if player1 == 'R':
        if player2 == 'S':
            print("Yaay! player1 is the winner as he has chosen ROCK and player2 has chosen SCISSORS")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif player2 == 'P':
            print("Yaay! player2 is the winner as he has chosen PAPER and player1 has chosen ROCK")
            print("Thanks for playing, have a nice day!")
            sys.exit()
        elif player2 == 'R':
            print("Oh No! Its a TIE as player1 and player2 have chosen ROCK")
            another_chance()
            sys.exit()
#-----------------------------------------------------------------------------------------------------

print("Assume, ROCK as 'R', SCISSORS as 'S', PAPER as 'P'")
print("Select your choice accordingly and enjoy the game. All the best!")

player1 = getpass.getpass("what's your choice player1: ")
player2 = getpass.getpass("what's your choice player2: ")

if player1 == 'P':
    if player2 == 'R':
        print("Yaay! player1 is the winner as he has chosen PAPER and player2 has chosen ROCK")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif player2 == 'S':
        print("Yaay! player2 is the winner as he has chosen SCISSORS and player1 has chosen PAPER")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif player2 == 'P':
        print("Oh No! Its a TIE as player1 and player2 have chosen PAPER")
        another_chance()
        sys.exit()

if player1 == 'S':
    if player2 == 'R':
        print("Yaay! player2 is the winner as he has chosen ROCK and player1 has chosen SCISSORS")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif player2 == 'P':
        print("Yaay! player1 is the winner as he has chosen SCISSORS and player2 has chosen PAPER")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif player2 == 'S':
        print("Oh No! Its a TIE as player1 and player2 have chosen SCISSORS")
        another_chance()
        sys.exit()


if player1 == 'R':
    if player2 == 'S':
        print("Yaay! player1 is the winner as he has chosen ROCK and player2 has chosen SCISSORS")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif player2 == 'P':
        print("Yaay! player2 is the winner as he has chosen PAPER and player1 has chosen ROCK")
        print("Thanks for playing, have a nice day!")
        sys.exit()
    elif player2 == 'R':
        print("Oh No! Its a TIE as player1 and player2 have chosen ROCK")
        another_chance()
        sys.exit()



