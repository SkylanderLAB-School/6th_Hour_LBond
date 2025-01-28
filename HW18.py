#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW18

import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
BeanBag = ["Black", "Refried", "Laser", "Beans from Rango", "Green"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def rand_bean():
    print(BeanBag)
    bean = BeanBag[random.randint(0,4)]
    print(bean)
    if bean in BeanBag:
        BeanBag.remove(bean)
        print(BeanBag)
    else:
        print("No Bean.")

    Re_Bean()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def Re_Bean():
    userInput = input("Would you like to pick again? Y/N: ")
    if userInput == "Y" or userInput == "y":
        rand_bean()
    elif userInput == "N" or userInput == "n":
        exit()
    else:
        print("Invalid input")
        Re_Bean()
#5. Call the #3 function at the bottom.
rand_bean()