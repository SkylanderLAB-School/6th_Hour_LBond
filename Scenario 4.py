#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 4


#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

#Step 1. Establish Variables
#Step 2. Make a loop
#Step 2a. Ask for a rating number
#Step 2b. Check if rating number is between 1 and 5
#Step 2c. If rating number is valid, add to total
#Step 3. Find and print the average

players = int(input("How many players are playing?: "))
total = int(0)
while players in range(1,16):
    rating = int(input("What is your rating?: "))
    if 0 < rating > 5:
        print("error")
        break
    else:
        added = total + rating
#if the rating has been added to the total an equal number of times to the players, then do average