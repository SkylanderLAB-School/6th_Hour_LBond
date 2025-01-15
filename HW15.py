#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"

#2. Create a def function that calculates the average of three numbers.

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.

#4. Create a def function that loops from 1 to the number put in the argument.

#5. Call all of the functions created in 1 - 4 with relevant arguments.



def hello_world():
    print("Hello World!")


def average(a, b, c):
    add = int(a + b + c)
    print(add / 3)


def animal_list(*animal):
    print("The third animal is:", animal[2])


def num_loop(a):
    for i in range(1, a + 1):
        print(i)


hello_world()
average(7,2,8)
animal_list("Cow", "Penguin", "Octopus", "Crocodile", "Axolotl")
num_loop(7)