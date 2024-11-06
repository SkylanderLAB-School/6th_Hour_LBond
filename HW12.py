#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW12
import time
#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.

#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)

#3. Create a for loop that prints 5 different animals from a list.

#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")


for i in range(5,0,-1):
    print(i)
    time.sleep(0.5)
else:
    print("Hello World!")
    time.sleep(0.5)
print("---")
time.sleep(0.5)
for j in range(1,31):
    if j % 2 == 0:
        print(j)
        time.sleep(0.5)
print("---")
time.sleep(0.5)
animals = ["Cat", "Octopus", "Shark", "Gobble Gobble Guy", "Rat"]
for a in animals:
    print(a)
    time.sleep(0.5)
print("---")
time.sleep(0.5)
wow = input("Come on, say something:")[::-1]
time.sleep(0.5)
for k in wow:
    print(k)
