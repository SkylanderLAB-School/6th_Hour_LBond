#Name: Logan Bond
#Class: 6th Hour
#Assigment: Scenario 6
import random

#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.

#Once that is done, to ensure that the average of the statblock is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (Scenario 7) and print the average.

#function that rolls 4 six-sided dice (d6), -
#sorts them from highest to lowest -
#add highest 3 together -
#add that result to a list outside the function
#six times total and the print
i = 0

Stat_Block = []

def dice_roll():
    global RL_1, RL_2, RL_3, RL_4, Roll_List, RollTotal, i, Stat_Block
    for i in range(0, 6):

        RL_1 = random.randint(1,6)
        RL_2 = random.randint(1, 6)
        RL_3 = random.randint(1, 6)
        RL_4 = random.randint(1, 6)

        Roll_List = [RL_1, RL_2, RL_3, RL_4]
        Roll_List.sort(reverse=True)
        RollTotal = Roll_List[0] + Roll_List[1] + Roll_List[2]
        Stat_Block.append(RollTotal)




dice_roll()
print("Here are your stats. Remember, invest in INT, sorcery is peak.")
print(Stat_Block)
