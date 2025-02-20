#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
num = int(input("gimme a number: "))
try:
    print(100/num)
except ZeroDivisionError:
    print("YOU CAN'T DIVIDE BY ZERO!")



#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    k = int(input("give me another number: "))
    print(k)
except ValueError:
    print("k is not a number")



#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
f = 5
while f >= 0:
    print(f)
    f -= 1
    if f < 0:
        raise Exception("f is less than 0")
