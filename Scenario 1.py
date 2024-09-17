#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 1
#Help from: https://www.pikminwiki.com/Piklopedia_(Pikmin_2) , Kyle

# Scenario 1:
# You are a programmer for a fledgling game developer. Your team lead
# has asked you to create a nested dictionary containing five enemy
# creatures (and their properties) for combat testing.
# Additionally, the testers are asking for a way to input changes to the enemy's
# damage for balancing, as well as having it print those changes to
# confirm they went through.
# It is up to you to decide what properties
# are important and the theme of the game.

enemyDict = {
    "Creeping Chrysanthemum" : {
        "Health" : 2500,
        "Weight" : 10,
        "Weakness" : "Luring and Swarming"
    },
    "Gatling Groink" : {
        "Health" : 1200,
        "Weight" : 10,
        "Weakness" : "Reds"
    },
    "Careening Dirigibug" : {
        "Health" : 1500,
        "Weight" : 3,
        "Weakness" : "Yellows"
    },
    "Man-at-Legs" : {
        "Health" : 2800,
        "Weight" : 5,
        "Weakness" : "Hiding and Yellows"
    },
    "Titan Dweevil" : {
        "Health" : 5000,
        "Weight" : 1,
        "Weakness" : "Yellows"
    }
}

while True:
    pikkies = input("What enemy do you want to chuck plants at?:")
    if pikkies in enemyDict:
        enemyDict[pikkies]["Health"] -= int(input("How much damage is delt?:"))
        print("Health left:",enemyDict[pikkies]["Health"])
    if enemyDict[pikkies]["Health"] == 0:
        break