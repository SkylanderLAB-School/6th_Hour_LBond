#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.


def RPS():
    print("1 is rock, 2 is paper, and 3 is scissors")
    p1 = int(input("Your move?: "))
    p2 = random.randint(1,3)

    print("You chose: ",p1)
    print("The other one chose: ",p2)

    if p1 == 1 and p2 == 2:
        print("You Lose")
    elif p1 == 1 and p2 == 3:
        print("You Win")
    elif p1 == 2 and p2 == 1:
        print("You Win")
    elif p1 == 2 and p2 == 3:
        print("You Lose")
    elif p1 == 3 and p2 == 1:
        print("You Lose")
    elif p1 == 3 and p2 == 2:
        print("You Win")
    else:
        print("Tie")

    def again():
        restart = input("Do you want to play again?: ")
        if restart == "yes":
            RPS()
        else:
            exit()
    again()

RPS()
