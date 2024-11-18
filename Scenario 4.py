#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 4
import statistics

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#WITH MY CHAOTIC NEUTRAL ALIGNMENT, I CHANGE THE PARAMETERS OF THIS ASSIGNMENT!!!!!
#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players -(up to 5)-, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

#num of players
#choose rating - rate
#average of all ratings

players = int(input("How many players are playing?: "))
#print num
#player 1 turn
#p1_rating = int(input("Player 1, how would you rate this model from 1-5?: "))
#print rating

#repeat for other players

p1_rating = int()
p2_rating = int()
p3_rating = int()
p4_rating = int()
p5_rating = int()

if players >= 1 and players <= 5:
    p1_rating = int(input("Player 1, how would you rate this model from 1-5?: "))
    print("You give them a:", p1_rating)
    if players >=2:
        p2_rating = int(input("Player 2, how would you rate this model from 1-5?: "))
        print("You give them a:", p2_rating)
        if players >= 3:
            p3_rating = int(input("Player 3, how would you rate this model from 1-5?: "))
            print("You give them a:", p3_rating)
            if players >= 4:
                p4_rating = int(input("Player 4, how would you rate this model from 1-5?: "))
                print("You give them a:", p4_rating)
                if players := 5:
                    p5_rating = int(input("Player 5, how would you rate this model from 1-5?: "))
                    print("You give them a:", p5_rating)
elif players < 1:
    print("Sorry, not enough players")
elif players > 5:
    print("Sorry, too many players")

if players >= 1 and players <= 5:
    print("Now, for the average score!")
    ratesum = p1_rating + p2_rating + p3_rating
    averate = ratesum/players
    print(averate)
