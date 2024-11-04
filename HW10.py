#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW10

import time
#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.

i = 5
while i >= 0:
    print(i)
    time.sleep(1)
    i -= 1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
time.sleep(1.5)

j = 30
while j >= 1:
    if (j % 2) == 0:
        print(j)
        time.sleep(1)
        j -= 1
    else:
        print("The number is not even.")
        time.sleep(1)
        j -= 1

#3. Create a while loop that repeats until the user
#inputs the number 0.


while True:
    time.sleep(1)
    num = int(input("Gimme a number: "))
    if num != 0:
        print("WRONG")
        continue
    else:
        print("CORRECT")
        break