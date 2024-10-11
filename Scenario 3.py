#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 3

import random

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4




#Party Dictionary Goes Here
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "ATK Mod." : 1,
        "Damage" : "2d6 + 3",
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "ATK Mod." : 2,
        "Damage" : "1d6 + 2",
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "ATK Mod." : 4,
        "Damage" : "1d10",
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "ATK Mod." : 3,
        "Damage" : "1d6 + 4",
    }
}


#Enemy Dictionary Goes Here
enemyDict = {
    "Creeping Chrysanthemum" : {
        "Health" : 16,
        "ATK Mod." :4 ,
        "AC" : 17,
        "Damage" : "1d1 + 12"
    },
    "Gatling Groink" : {
        "Health" : 15,
        "ATK Mod." : 3,
        "AC" : 17,
        "Damage" : "1d1 + 12"
    },
    "Careening Dirigibug" : {
        "Health" : 10,
        "ATK Mod." : 1,
        "AC" : 7,
        "Damage" : "1d1 + 12"
    },
    "Man-at-Legs" : {
        "Health" : 20,
        "ATK Mod." : 5,
        "AC" : 15,
        "Damage" : "1d1 + 12"
    },
    "Titan Dweevil" : {
        "Health" : 25,
        "ATK Mod." : 2,
        "AC" : 12,
        "Damage" : "1d1 + 12"
    }
}


#Combat Vars
#---KEY---
#

atk0 = int(random.randint(1,10))#Gale atk roll
atk1 = int(random.randint(1,1) + 12)#Man-At-Legs atk roll
hit0 = int(random.randint(1,20) + 4)#Gale hit check
hit1 = int(random.randint(1,20) + 5)#M-A-L hit check
dam0 = int(enemyDict["Man-at-Legs"]["Health"] - atk0)
dam1 = int(partyDictionary["Gale"]["Health"] - atk1)
print("Gale's damage, if he hits:")
print(atk0)
print("---")
print("Gale's ATK roll:")
print(hit0)
print("---")
print("Man-At-Legs AC:")
print(enemyDict["Man-at-Legs"]["AC"])
print("---")
print("Man-At-Legs health post math crap:")
if hit0 >= enemyDict["Man-at-Legs"]["AC"]:
    print(dam0)
else:
    print("womp womp, no hit")

print("                 ")
print("                 ")
print("The Man-At-Legs' damage, if it hits:")
print(atk1)
print("---")
print("The Man-At-Legs' ATK roll:")
print(hit1)
print("---")
print("Gale's AC:")
print(partyDictionary["Gale"]["AC"])
print("---")
print("Gale's health post math crap:")
if hit1 >= partyDictionary["Gale"]["AC"]:
    print(dam1)
else:
    print("womp womp, no hit")


