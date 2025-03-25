#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW24

import random, time
import random
import time
#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Character:
    def __init__(self, health, damage, speed, maxHP):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.maxHP = maxHP
    def dmg_loop(self):
        for i in range(1, 11):
            self.health -= random.randint(1, 6)
            print("The party member took Damage. Their health is now:")
            print(self.health)
            print(" ")
            time.sleep(1)
    def E_key (self):
        self.health += 30
        if self.health > 100:
            self.health = 100
#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = Character(100, 20, 30, 100)
healer = Character(60,10,30, 60)
thief = Character(50, 30, 40, 50)
mage = Character(45, 35, 25, 45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
randomPoison = int(random.randint(1,4))
if randomPoison == 1:
    print("The Warrior got rotted!")
    warrior.dmg_loop()
elif randomPoison == 2:
    print("The Healer got rotted!")
    healer.dmg_loop()
elif randomPoison == 3:
    print("The Thief got rotted!")
    thief.dmg_loop()
elif randomPoison == 4:
    print("The Mage got rotted!")
    mage.dmg_loop()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
if warrior.health < warrior.maxHP:
    warrior.E_key()
    print("The Warrior was healed! Their Health is now:")
    print(warrior.health)
if healer.health < healer.maxHP:
    healer.E_key()
    print("The Healer was healed! Their Health is now:")
    print(healer.health)
if thief.health < thief.maxHP:
    thief.E_key()
    print("The Thief was healed! Their Health is now:")
    print(thief.health)
if mage.health < mage.maxHP:
    mage.E_key()
    print("The Mage was healed! Their Health is now:")
    print(mage.health)
