#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!

#2. Create three different boolean variables named wifi, login, and admin.

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

import random
import time
print("Hello World!")
wifi = random.randint(1,2) == 1
login = random.randint(1,2) == 1
admin = random.randint(1,2) == 1
lognum = 0
print("Times logged in:", lognum)
begin = input("Do you want to log in?: ")
if begin == "Yes" :
    time.sleep(1)
    print("Logging in.")
    time.sleep(1)
    if wifi :
        if login :
            if admin :
                print("Welcome.")
                lognum += 1
                print("Times logged in:", lognum)
            else:
                print("ERROR: You aren't an admin dum-dum.")
        else:
            print("ERROR: You have to log in before you can log in.")
    else:
        print("ERROR: How are you even attempting this? YOU HAVE NO WIFI!")