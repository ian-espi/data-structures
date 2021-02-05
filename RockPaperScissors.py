# name: Ian Espinosa
# email: IanEspinosaBiz@gmail.com
# program: Rock_Paper_Scissors

import random
while True:

    user = input("Enter your choice:\n"
                 "R or r for rock\n"
                 "P or p for paper\n"
                 "S or s for scissors\n"
                 "Q or q to quit\n")
    user = user.lower()

    if user == "r":
        user = "rock"
    if user == "p":
        user = "paper"
    if user == "s":
        user = "scissors"
    if user == "q":
        break

    comptInt = random.randrange(0, 3)
    if comptInt == 0:
        computer = "rock"
    elif comptInt == 1:
        computer = "paper"
    elif comptInt == 2:
        computer = "scissors"
    else:
        computer = "void"

    if user == computer:
        print("Computer picked:", computer)
        print("You tie against the computer")
    elif user == "rock":
        if computer == "paper":
            print("Computer picked:", computer)
            print("You lose against the computer")
        else:
            print("Computer picked:", computer)
            print("You win against the computer")
    elif user == "paper":
        if computer == "rock":
            print("Computer picked:", computer)
            print("You win against the computer")
        else:
            print("Computer picked:", computer)
            print("You lose against the computer")
    elif user == "scissors":
        if computer == "rock":
            print("Computer picked:", computer)
            print("You lose against the computer")
        else:
            print("Computer picked:", computer)
            print("You win against the computer")
