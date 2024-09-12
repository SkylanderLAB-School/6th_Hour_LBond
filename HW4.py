# Name: Logan Bond
# Class: 6th Hour
# Assignment: HW4
# Help from: https://github.com/CoachMack/6th-Hour-CompSci/blob/master/DictionariesLecture.py,

#1.print hello world -
#2.create a dictionary with 3 keys and a value for each key -
#2a.one of the keys must have a value with a list containing three numbers inside -
#3.print one of the three numbers by itself -
#4.using the update function, add a fourth key to the dictionary and give it a value -
#5.print the entire dictionary -
#6.clear all of the data inside of the dictionary and print it -
#7.make a nested dictionary with 3 entries containing the name of another classmate and two other pieces of information within each entry -
#8.print the names of all three classmates on the same line -

print("Hello World")

TF2pickDict = {
    "Attack" : "Demoman/Pyro",
    "Defence" : "Engineer/Pyro",
    "Average" : [24,26,50]
}
print(TF2pickDict)

print(TF2pickDict["Average"][2])

TF2pickDict.update({"Main" : "Pyro"})

print(TF2pickDict)

TF2pickDict.clear()
print(TF2pickDict)

classmateDict = {
    "mate1" : {
        "name" : "Kyle",
        "short" : "yes",
        "age" : "IDK"
    },
    "mate2" : {
        "name" : "Ryan",
        "short" : "yes",
        "age" : "IDK"
    },
    "mate3" : {
        "name" : "CJ",
        "short" : "no",
        "age" : "IDK"
    }
}
print(classmateDict["mate1"]["name"],classmateDict["mate2"]["name"],classmateDict["mate3"]["name"])