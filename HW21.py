#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sportDict = {
    "sport1" : {
        "Name" : "Marching Band",
        "Players" : 60,
        "Ball" : False,
    },
    "sport2": {
        "Name" : "Basketball",
        "Players" : 5,
        "Ball" : True,
    },
    "sport3": {
        "Name" : "Bollyball",
        "Players" : 6,
        "Ball" : True,
    }
}

#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def Player_Add (a, b, c):
    global sportDict
    print(a + b + c)

#3. Call the function with arguments here
Player_Add(a=sportDict["sport1"]["Players"], b=sportDict["sport2"]["Players"], c=sportDict["sport3"]["Players"])

