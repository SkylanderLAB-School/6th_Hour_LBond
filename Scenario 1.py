#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 1
#Help from: https://www.pikminwiki.com/Piklopedia_(Pikmin_2) ,

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
    "foe1" : {
        "Name" : "Creeping Chrysanthemum",
        "Health" : "2500",
        "Weight" : "10",
        "Weakness" : "Luring and Swarming"
    },
    "foe2" : {
        "Name" : "Gatling Groink",
        "Health" : "1200",
        "Weight" : "10",
        "Weakness" : "Reds"
    },
    "foe3" : {
        "Name" : "Careening Dirigibug",
        "Health" : "1500",
        "Weight" : "3",
        "Weakness" : "Yellows"
    },
    "foe4" : {
        "Name" : "Man-at-Legs",
        "Health" : "2800",
        "Weight" : "5",
        "Weakness" : "Hiding and Yellows"
    },
    "foe5" : {
        "Name" : "Titan Dweevil",
        "Health" : "5000/6000",
        "Weight" : "30/30/30/30/1",
        "Weakness" : "Yellows"
    }
}

enemyDict["foe3"]["Health"] = int(input("Damage Delt:",))
print(enemyDict[foe3])