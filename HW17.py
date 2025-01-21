#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW17
import random

#1. Import the "random" library and create a def function that prints "Hello World!"

#2. Create two empty integer variables named "heads" and "tails"

#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.

#4. Call the "Hello world" and "Coin Flip" functions here

#5. Print the final result of heads and tails here
def hole_A():
    print("Hello World!")


heads = int()
tails = int()

def coin_flip():
    global heads
    global tails
    for i in range(1,101):
        flip = random.randint(1,2)
        if flip == 1:
            heads += 1
        else:
            tails += 1


hole_A()
coin_flip()
print(heads)
print(tails)
