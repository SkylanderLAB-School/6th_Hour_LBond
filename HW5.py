#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW5

import random
#1. Print "Hello World!"
print("Hello World!")

#2. Create a list that contains 3 integers
numlist = [random.randint(1,1000), random.randint(1,1000), random.randint(1,1000)]
print(numlist)

#3. Create an if statement that prints out whichever of the three numbers is the highest
if numlist[0] >= numlist[1] and numlist[0] >= numlist[2] :
    print(numlist[0], "is the biggest number.")
elif numlist[1] >= numlist[2] and numlist[1] >= numlist[0]  :
    print(numlist[1], "is the biggest number.")
elif numlist[2] >= numlist[1] and numlist[2] >= numlist[0] :
    print(numlist[2], "is the biggest number.")

print(max(numlist), "is the biggest number")

