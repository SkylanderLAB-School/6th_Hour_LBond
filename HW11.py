#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW11
import time
#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
F = 1

while F <= 100:
    if F % 3 == 0:
        if F % 5 == 0:
            print("Fizz Buzz")
            time.sleep(1)
            F += 1
            continue
        else:
            print("Fizz")
            time.sleep(1)
            F += 1
            continue
    else:
        if F % 5 == 0:
            print("Buzz")
            time.sleep(1)
            F += 1
            continue
        else:
            print(F)
            time.sleep(1)
            F += 1
            continue
