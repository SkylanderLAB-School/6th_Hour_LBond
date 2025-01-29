#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW18
import time
import random
i = 4
#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
BeanBag = ["Black", "Refried", "Laser", "Beans from Rango", "Green"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def rand_bean():
    global i
    print(BeanBag)
    time.sleep(1)
    bean = BeanBag[random.randint(0,i)]
    print(bean)
    time.sleep(1)
    if bean in BeanBag:
        BeanBag.remove(bean)
        print(BeanBag)
        time.sleep(1)
        i-=1
    if i == -1:
        time.sleep(1)
        print("No Beans Left!")
        exit()
    Re_Bean()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def Re_Bean():
    userInput = input("Would you like to pick again? Y/N: ")
    time.sleep(1)
    if userInput == "Y" or userInput == "y":
        rand_bean()
    elif userInput == "N" or userInput == "n":
        exit()
    else:
        print("Invalid input")
        Re_Bean()
#5. Call the #3 function at the bottom.
hello_world()
rand_bean()