#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 2
#Help from:

#Scenario 2:
#The programmer in charge of the player character party stats is
#having some issues with their code. Despite rigorous testing,
#they are inexperienced and can't seem to figure out why it damage
#testing isn't working. Your team lead has asked you to help by fixing
#the party dictionary, insert an enemy into the code below, and
#testing to see if a player character can damage the with a printed
#test that shows the enemy health has changed.


partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}

#Enemy Dictionary goes here
enemyDict = {
    "Creeping Chrysanthemum" : {
        "Health" : 50,
        "Weight" : 10,
        "Weakness" : "Luring and Swarming",
        "Damage" : 9999999999999999999999
    },
    "Gatling Groink" : {
        "Health" : 25,
        "Weight" : 10,
        "Weakness" : "Reds",
        "Damage" : 9999999999999999999999
    },
    "Careening Dirigibug" : {
        "Health" : 20,
        "Weight" : 3,
        "Weakness" : "Yellows",
        "Damage" : 9999999999999999999999
    },
    "Man-at-Legs" : {
        "Health" : 75,
        "Weight" : 5,
        "Weakness" : "Hiding and Yellows",
        "Damage" : 9999999999999999999999
    },
    "Titan Dweevil" : {
        "Health" : 125,
        "Weight" : 1,
        "Weakness" : "Yellows",
        "Damage" : 9999999999999999999999
    }
}


#Test the damage here by subtracting a party member's damage from the enemy's health.
while True:
    Chara = input("Who is attacking?:")
    ATK = input("What enemy do you want to attack?:")
    if ATK in enemyDict:
        enemyDict[ATK]["Health"] -= partyDictionary[Chara]["Damage"]
        print(ATK, "health left:",enemyDict[ATK]["Health"])
    if enemyDict[ATK]["Health"] <= 0:
        break