# Name: Logan Bond
# Class: 6th Hour
# Assignment: Playground
# Help From : Kyle

#Hello World statement
print("Hello World")


#Intro and Instuctions
print("WELCOME TO MY PLAYGROUND! YES, IT IS AN ACTUAL PLAYGROUND!")
print("Here at the playground, we have many fun things!")
print("We have the: 'Monkey Bars', 'Metal Slide', 'Swing Set', and 'Merry-Go-Round'. Or you could go 'Home'")
print("(to go to the location where you want to go to, type it EXACTLY as you see it between the two [']'s ['example'])")

#haha, this is intended to be a Diary of Wimpy Kid reference
while True:
    location = input("Where do you want to go?:")

    if location == "Monkey Bars" :
        print("Sorry, they were removed for some stupid kids breaking 3 ribs on them.")

    if location == "Metal Slide" :
        print("Sorry, they were removed for kids losing their entire back from 427th degree burns.")

    if location == "Swing Set" :
        print("Well, there is a swing open, but it's the 'bad swing'. Maybe something else would be more fun.")

    if location == "Home" :
        print("you cant go home.")

    if location == "example":
        print("^^vv<><>BA-")

    if location == "Merry-Go-Round":
        print("Good choice!")
        break

print("Now comes an important question. Go left or go right?")
direction = input("Go ")

if direction == "left" :
    print("Alright, then start spinning left!")
    print("As you spin left, you go faster and faster, even without another master!")
    print("But, just as you started to have fun, your mom says it's time to go home...")
    print("Goodbye")


if direction == "right" :
    print("As you start to spin to the right, a squeaky wheel begins to squeak")
    print("This causes your ears to bleed and you to go to the hospital.")
    print("[Insert Dark Souls: 'YOU DIED' here]")


ending = input("GAME OVER, RESTART?:")
if ending == "yes":
    print("Too bad, womp womp, you gotta do chores.")

if ending == "^^vv<><>BA-" :
    print("Hey, good job. You did the thing I hid VERY well...You know, I had a reward planned out, but I forgot it by turning my brain off and playing Pizza Tower...")
