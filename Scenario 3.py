#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario 3

import random
import time

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
        "Damage" : random.randint(2,12) + 3
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "ATK Mod." : 2,
        "Damage" : random.randint(1,6) + 2
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "ATK Mod." : random.randint(1,20) + 4,
        "Damage" : random.randint(1,10)
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "ATK Mod." : 3,
        "Damage" : random.randint(1,6) + 4
    }
}


#Enemy Dictionary Goes Here
enemyDict = {
    "Creeping Chrysanthemum" : {
        "Health" : 16,
        "ATK Mod." :4 ,
        "AC" : 17,
        "Damage" : random.randint(1,1) + 12
    },
    "Gatling Groink" : {
        "Health" : 15,
        "ATK Mod." : 3,
        "AC" : 17,
        "Damage" : random.randint(1,1) + 12
    },
    "Careening Dirigibug" : {
        "Health" : 10,
        "ATK Mod." : 1,
        "AC" : 7,
        "Damage" : random.randint(1,1) + 12
    },
    "Man-at-Legs" : {
        "Health" : 20,
        "ATK Mod." : random.randint(1,20) + 5,
        "AC" : 15,
        "Damage" : random.randint(1,1) + 12
    },
    "Titan Dweevil" : {
        "Health" : 25,
        "ATK Mod." : 2,
        "AC" : 12,
        "Damage" : random.randint(1,1) + 12
    }
}


#Combat Vars
#---KEY---
#Ugly Alien - LZ
#Sus Girl - SH
#MAGIC - GL
#Nic Cage - AS
#Flower - CC
#Gun Boi - GG
#Hiroshima - CD
#Gun Spider - MAL
#Big Spider - TD

#Party Damage and Hit Checks
#LZATK = int(partyDictionary["LaeZel"]["Damage"])
#LZHIT = int(random.randint(1,20) + partyDictionary["LaeZel"]["ATK Mod."])
#
#SHATK = int(partyDictionary["Shadowheart"]["Damage"])
#SHHIT = int(random.randint(1,20) + partyDictionary["Shadowheart"]["ATK Mod."])
#
#GLATK = int(partyDictionary["Gale"]["Damage"])
#GLHIT = int(random.randint(1,20) + partyDictionary["Gale"]["ATK Mod."])
#
#ASATK = int(partyDictionary["Astarion"]["Damage"])
#ASHIT = int(random.randint(1,20) + partyDictionary["Astarion"]["ATK Mod."])
#
#Enemy Damage and Hit Checks
#CCATK = int(enemyDict["Creeping Chrysanthemum"]["Damage"])
#CCHIT = int(random.randint(1,20) + enemyDict["Creeping Chrysanthemum"]["ATK Mod."])
#
#GGATK = int(enemyDict["Gatling Groink"]["Damage"])
#GGHIT = int(random.randint(1,20) + enemyDict["Gatling Groink"]["ATK Mod."])
#
#CDATK = int(enemyDict["Careening Dirigibug"]["Damage"])
#CDHIT = int(random.randint(1,20) + enemyDict["Careening Dirigibug"]["ATK Mod."])
#
#MALATK = int(enemyDict["Man-at-Legs"]["Damage"])
#MALHIT = int(random.randint(1,20) + enemyDict["Man-at-Legs"]["ATK Mod."])
#
#TDATK = int(enemyDict["Titan Dweevil"]["Damage"])
#TDHIT = int(random.randint(1,20) + enemyDict["Titan Dweevil"]["ATK Mod."])
#

CHA = input("Who is attacking?:")
ENM = input("Who is being attacked?:")

#Gale VS Man-at-Legs
if CHA == "Gale":
    if ENM == "Man-at-Legs":
        while True:
            time.sleep(1.5)
            print("Gale's health:")
            print(partyDictionary["Gale"]["Health"])
            print("---")
            time.sleep(1.5)
            print("Man-at-Legs health:")
            print(enemyDict["Man-at-Legs"]["Health"])
            print("---")
            time.sleep(1.5)
            print("Gale's damage, if he hits:")
            print(partyDictionary["Gale"]["Damage"])
            print("---")
            time.sleep(1.5)
            print("Gale's ATK roll:")
            print(partyDictionary["Gale"]["ATK Mod."])
            print("---")
            time.sleep(1.5)
            print("Man-At-Legs AC:")
            print(enemyDict["Man-at-Legs"]["AC"])
            print("---")
            time.sleep(1.5)
            print("Man-At-Legs health post math crap:")
            if GLHIT >= enemyDict["Man-at-Legs"]["AC"]:
                enemyDict["Man-at-Legs"]["Health"] -= GLATK
                print(enemyDict["Man-at-Legs"]["Health"])
            else:
                print("ATK did not hit")
            print("                 ")
            time.sleep(1.5)
            print("Man-at-Legs health:")
            print(enemyDict["Man-at-Legs"]["Health"])
            print("---")
            time.sleep(1.5)
            print("Gale's health:")
            print(partyDictionary["Gale"]["Health"])
            print("---")
            time.sleep(1.5)
            print("                 ")
            print("Man-at-Legs damage, if it hits:")
            print(MALATK)
            print("---")
            time.sleep(1.5)
            print("M-A-L ATK roll:")
            print(MALHIT)
            print("---")
            time.sleep(1.5)
            print("Gale's AC:")
            print(partyDictionary["Gale"]["AC"])
            print("---")
            time.sleep(1.5)
            print("Gale's health post math crap:")
            if MALHIT >= partyDictionary["Gale"]["AC"]:
                partyDictionary["Gale"]["Health"] -= MALATK
                print(partyDictionary["Gale"]["Health"])
            else:
                print("ATK did not hit")
            if enemyDict["Man-at-Legs"]["Health"] <= 0:
                print("The Man-at-Legs died, YOU WIN!")
                break
            elif partyDictionary["Gale"]["Health"] <= 0:
                print("Gale died, you lose.")
                break

#Gale VS Creeping Flower boi
if CHA == "Gale":
    if ENM == "Creeping Chrysanthemum":
        while True:
            time.sleep(1.5)
            print("Gale's damage, if he hits:")
            print(GLATK)
            print("---")
            time.sleep(1.5)
            print("Gale's ATK roll:")
            print(GLHIT)
            print("---")
            time.sleep(1.5)
            print("Creeping Chrysanthemum AC:")
            print(enemyDict["Creeping Chrysanthemum"]["AC"])
            print("---")
            time.sleep(1.5)
            print("Creeping Chrysanthemum health post math crap:")
            if GLHIT >= enemyDict["Creeping Chrysanthemum"]["AC"]:
                enemyDict["Creeping Chrysanthemum"]["Health"] -= GLATK
                print(enemyDict["Creeping Chrysanthemum"]["Health"])
            else:
                print("ATK did not hit")
            print("                 ")
            time.sleep(1.5)
            print("                 ")
            print("Creeping Chrysanthemum damage, if it hits:")
            print(CCATK)
            print("---")
            time.sleep(1.5)
            print("Creeping Chrysanthemum ATK roll:")
            print(CCHIT)
            print("---")
            time.sleep(1.5)
            print("Gale's AC:")
            print(partyDictionary["Gale"]["AC"])
            print("---")
            time.sleep(1.5)
            print("Gale's health post math crap:")
            if MALHIT >= partyDictionary["Gale"]["AC"]:
                partyDictionary["Gale"]["Health"] -= CCATK
                print(partyDictionary["Gale"]["Health"])
            else:
                print("ATK did not hit")
            if enemyDict["Creeping Chrysanthemum"]["Health"] <= 0:
                print("The Creeping Chrysanthemum died, YOU WIN!")
                break
            elif partyDictionary["Gale"]["Health"] <= 0:
                print("Gale died, you lose.")
                break























#dam0 = int(enemyDict["Man-at-Legs"]["Health"] - atk0)
#dam1 = int(partyDictionary["Gale"]["Health"] - atk1)
#print("Gale's damage, if he hits:")
#print()
#print("---")
#print("Gale's ATK roll:")
#print()
#print("---")
#print("Man-At-Legs AC:")
#print(enemyDict["Man-at-Legs"]["AC"])
#print("---")
#print("Man-At-Legs health post math crap:")
#if  >= enemyDict["Man-at-Legs"]["AC"]:
#    print()
#else:
#    print("womp womp, no hit")

#print("                 ")
#print("                 ")
#print("The Man-At-Legs' damage, if it hits:")
#print()
#print("---")
#print("The Man-At-Legs' ATK roll:")
#print()
#print("---")
#print("Gale's AC:")
#print(partyDictionary["Gale"]["AC"])
#print("---")
#print("Gale's health post math crap:")
#if  >= partyDictionary["Gale"]["AC"]:
#    print()
#else:
#    print("womp womp, no hit")
