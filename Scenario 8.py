#Name: Logan Bond
#Class: 6th Hour
#Assignment: Scenario8
import random



#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

class Character:
    def __init__(self, name, species, type, health, ac, atk_mod, damage):
        self.name = name
        self.species = species
        self.type = type
        self.health = health
        self.ac = ac
        self.atk_mod = atk_mod
        self.damage = damage



#Characters
#LaeZel
#Shadowheart
#Gale
#Astarion

#Enemies
#Creeping Chrysanthemum
#Gatling Groink
#Careening Dirigibug
#Man-at-Legs
#Titan Dweevil


Laezel = Character("LaeZel", "Githyanki", "Fighter", 12, 17, 1, random.randint(2,12) + 3)
SHeart = Character("Shadowheart", "Half-Elf", "Cleric", 10, 14, 2, random.randint(1,6) + 2)
Gale = Character("Gale", "Human", "Wizard", 8, 14, random.randint(1,20) + 4, random.randint(1,10))
Astarion = Character("Astarion", "High Elf", "Rouge", 10, 14, 3, random.randint(1,6) + 4)

Creeping = Character("Creeping Chrysanthemum", "Taraxacum rovinia", "Chrysanthemum", 16, 17, 4, 13)
Groink = Character("Gatling Groink", "Megaplod calibersi", "Unknown", 15, 17, 3, 13)
Dirigibug = Character("Careening Dirigibug", "Flotillium circusmaximus", "Dirigibug", 10, 7, 1, 13)
MAL = Character("Man-at-Legs", "Pseudoarachnia navaronia", "Arachnorb", 20, 15, random.randint(1,20) + 5, 13)
Dweevil = Character("Titan Dweevil", "Mandarachnia gargantium", "Dweevil", 25, 12, 2, 13)

print("Man-at-Legs health")
print(MAL.health)
print("---")
print("Gale health")
print(Gale.health)
print("---")
print("Gale is attacking!")
print("...")

if random.randint(1,20) + Gale.atk_mod >= MAL.ac:
    MAL.health -= Gale.damage
    if MAL.health <= 0:
        print("The Man-at-Legs was hit, and died. You Win!")
        exit()
    else:
        print("The Man-at-Legs was hit, but is alive....R U N")
else:
    print("Gale missed...R U N")

print("The Man-at-Legs is firing!")
print("...")

if random.randint(1,20) + MAL.atk_mod >= Gale.ac:
    Gale.health -= MAL.damage
    if Gale.health <= 0:
        print("Gale was hit, and died. You Lose.")
        exit()
    else:
        print("Gale was hit, and is alive.")
else:
    print("The Man-at-Legs missed, good job.")


'''
if random.randint(1,20) + partyDict["Shadowheart"]["AtkMod"] >= enemyDict["Goblin"]["AC"]:
#   We hit! Deal Damage (subtract Party Damage Roll from HP)
    enemyDict["Goblin"]["Health"] -= partyDict["Shadowheart"]["Damage"]
    #Check to see if enemy is dead
    if enemyDict["Goblin"]["Health"] <= 0:
        print("Gobbo was hit! Gobbo is dead!")
        exit()
    #else, go to enemy turn
    else:
        print("Gobbo was hit! Gobbo is still alive!")
#else, we miss
else:
    print("Shadowheart Missed!")

if random.randint(1,20) + enemyDict["Goblin"]["AtkMod"] >= partyDict["Shadowheart"]["AC"]:
    partyDict["Shadowheart"]["Health"] -= enemyDict["Goblin"]["Damage"]
    if partyDict["Shadowheart"]["Health"] <= 0:
        print("Gobbo hit! Shadowheart is down!")
        exit()
    else:
        print("Gobbo hit! Shadowheart is alive!")
else:
    print("No one hit!")
'''