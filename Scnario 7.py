#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
from Scnario_6 import *
listAverage = 0

def final_average():
    global listAverage
    listAverage = (Stat_Block[0] + Stat_Block[1] + Stat_Block[2] + Stat_Block[3] + Stat_Block[4] + Stat_Block[5])/6#Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print("Here is the average of your stats.")
print(listAverage)