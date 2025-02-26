import time
#NG LOCATIONS:
#10 - 53 - 100 - 156 - 211 - 269
#NG - +  -  +1 -  +2 -  +3 -  +4

#make def function
#have a counter in function for ng level
#do ng, but if any other option is picked, do something
#once ng is done, and repeat is selected, increace counter and allow more options.

location_list = ["Merry-Go-Round", "Swing Set", "Metal Slide", "Monkey Bars", "^^vv<><>BA+", "Alone! Infection! Void! S**t attacking from the other side, yuck! Alone! Infection! Chaos! A-B-C-D-E-F, go! Checkmate (checkmate), informed consent (oh, yeah). It increases words. Relation (relation). Duration (oh, yeah). Build and realize. MESSIAH! Will not come. Parallax! Paradox! Paradigm will attack! We've got only one sky! Blue, red, and black paranoia. What is it like to you? No one can see the colors but you! Alone! Infection! Void! S**t attacking from the other side yuck! Alone! Infection! Chaos! A-B-C-D-E-F, go! Light and darkness invisible (oh, yeah). Your soul dissipates. Destruction  re-reduction (oh, yeah). TOWER OF BABEL! MESSIAH! Will not come. Parallax! Paradox! Paradigm will attack! We've got only one sky! Blue, red, and black paranoia. What is it like to you? No one can see the colors but you! ...I had to run away from here...Before the storm hit...We see eye to eye...We see eye to eye...I told me, without you! We've got only one sky! Blue, red, and black (BLUE, RED, AND BLACK) paranoia (paranoia)! What is it like to you? (LIKE TO YOU!) No one can see the colors but you! We've got only one sky! Joy, grief, and fun PARANOIA! What is it like to you? No one can see the colors, the colors, but you!"]


def Playground ():
    global i
    i = 1
    if i == 1:
        print("We currently only have a ", location_list[0])
    elif i == 2:
        print("We currently only have a ", location_list[0], "and ", location_list[1])
    elif i == 3:
        print("We currently only have a ", location_list[0], location_list[1], "and ", location_list[2])
    elif i == 4:
        print("We currently only have a ", location_list[0], location_list[1], location_list[2], "and ", location_list[3])
        print("Or, you could go 'home'")

    Choose = input("Where do you want to go?: ")

    if Choose == location_list[0]:
        print("Good Choice!")
        TheRest()
    elif Choose == location_list[0]:


    elif Choose == "example":
        print(location_list[4])
        print("I'll just assume you chose the Merry-Go-Round")
        TheRest()





def TheRest ():
    time.sleep(1.5)
    print("Now comes an important question. Spin left or go right?")
    direction = input("Go ")
    if direction == "left":
        time.sleep(1.5)
        print("Alright, then start spinning left!")
        time.sleep(1.5)
        print("As you spin left, you go faster and faster, even without another master!")
        time.sleep(1.5)
        print("But, just as you started to have fun, your mom says it's time to go home...")
        time.sleep(1.5)
        print("Goodbye")
    if direction == "right":
        time.sleep(1.5)
        print("As you start to spin to the right, a squeaky wheel begins to squeak")
        time.sleep(1.5)
        print("This causes your ears to bleed and you to go to the hospital.")
        time.sleep(1.5)
        print("[Insert Dark Souls: YOU DIED here]")
    time.sleep(1.5)
    ending = input("GAME OVER, RESTART?:")
    if ending == "Yes":
        time.sleep(1.5)
        print("Too bad, womp womp, you gotta do chores.")
        exit()
    elif ending == location_list[4]:
        i += 1
        Playground()



Playground()






"""
#NEW GAME
print("WELCOME TO MY PLAYGROUND! YES, IT IS AN ACTUAL PLAYGROUND!")
time.sleep(1.5)
print("Here at the playground, we have many fun things!")
time.sleep(1.5)
print("We currently only have a 'Merry-Go-Round' however...")
print("(to go to the location where you want to go to, type it EXACTLY as you see it between the two [']'s ['example'])")
time.sleep(1.5)
while True:
    location = input("Where do you want to go?:")
    if location == "example":
        time.sleep(1.5)
        print("^^vv<><>BA-")
    if location == "Merry-Go-Round":
        time.sleep(1.5)
        print("Good choice!")
        break
time.sleep(1.5)
print("Now comes an important question. Spin left or go right?")
direction = input("Go ")
if direction == "left" :
    time.sleep(1.5)
    print("Alright, then start spinning left!")
    time.sleep(1.5)
    print("As you spin left, you go faster and faster, even without another master!")
    time.sleep(1.5)
    print("But, just as you started to have fun, your mom says it's time to go home...")
    time.sleep(1.5)
    print("Goodbye")
if direction == "right" :
    time.sleep(1.5)
    print("As you start to spin to the right, a squeaky wheel begins to squeak")
    time.sleep(1.5)
    print("This causes your ears to bleed and you to go to the hospital.")
    time.sleep(1.5)
    print("[Insert Dark Souls: YOU DIED here]")
time.sleep(1.5)
ending = input("GAME OVER, RESTART?:")
if ending == "Yes":
    time.sleep(1.5)
    print("Too bad, womp womp, you gotta do chores.")
if ending == "^^vv<><>BA-" :
    time.sleep(2)
#NG+
    print("WELCOME TO MY PLAYGROUND! YES, IT IS AN ACTUAL PLAYGROUND! - NG+")
    time.sleep(1.5)
    print("Here at the playground, we have many fun things!")
    time.sleep(1.5)
    print("We have a 'Swing Set' and 'Merry-Go-Round'.")
    print(
        "(to go to the location where you want to go to, type it EXACTLY as you see it between the two [']'s ['example'])")
    time.sleep(1.5)
    while True:
        location = input("Where do you want to go?:")
        if location == "Swing Set":
            time.sleep(1.5)
            print("Well, there is a swing open, but it's the 'bad swing'. Maybe something else would be more fun.")
        if location == "example":
            time.sleep(1.5)
            print("^^vv<><>BA-")
        if location == "Merry-Go-Round":
            time.sleep(1.5)
            print("Good choice!")
            break
    time.sleep(1.5)
    print("Now comes an important question. Spin left or go right?")
    direction = input("Go ")
    if direction == "left":
        time.sleep(1.5)
        print("Alright, then start spinning left!")
        time.sleep(1.5)
        print("As you spin left, you go faster and faster, even without another master!")
        time.sleep(1.5)
        print("But, just as you started to have fun, your mom says it's time to go home...")
        time.sleep(1.5)
        print("Goodbye")
    if direction == "right":
        time.sleep(1.5)
        print("As you start to spin to the right, a squeaky wheel begins to squeak")
        time.sleep(1.5)
        print("This causes your ears to bleed and you to go to the hospital.")
        time.sleep(1.5)
        print("[Insert Dark Souls: YOU DIED here]")
    time.sleep(1.5)
    ending = input("GAME OVER, RESTART?:")
    if ending == "Yes":
        time.sleep(1.5)
        print("Too bad, womp womp, you gotta do chores.")
    if ending == "^^vv<><>BA-":
        time.sleep(2)
#NG+1
        print("WELCOME TO MY PLAYGROUND! YES, IT IS AN ACTUAL PLAYGROUND! - NG+1")
        time.sleep(1.5)
        print("Here at the playground, we have many fun things!")
        time.sleep(1.5)
        print("We have a 'Swing Set', and 'Merry-Go-Round'. Or you could go 'Home'")
        print(
            "(to go to the location where you want to go to, type it EXACTLY as you see it between the two [']'s ['example'])")
        time.sleep(1.5)
        while True:
            location = input("Where do you want to go?:")
            if location == "Monkey Bars":
                time.sleep(1.5)
                print("Sorry, they were removed for some stupid kids breaking 3 ribs on them.")
            if location == "Metal Slide":
                time.sleep(1.5)
                print("Sorry, they were removed for kids losing their entire back from 427th degree burns.")
            if location == "Swing Set":
                time.sleep(1.5)
                print("Well, there is a swing open, but it's the 'bad swing'. Maybe something else would be more fun.")
            if location == "Home":
                time.sleep(1.5)
                print("you cant go home.")
            if location == "example":
                time.sleep(1.5)
                print("^^vv<><>BA-")
            if location == "Merry-Go-Round":
                time.sleep(1.5)
                print("Good choice!")
                break
        time.sleep(1.5)
        print("Now comes an important question. Spin left or go right?")
        direction = input("Go ")
        if direction == "left":
            time.sleep(1.5)
            print("Alright, then start spinning left!")
            time.sleep(1.5)
            print("As you spin left, you go faster and faster, even without another master!")
            time.sleep(1.5)
            print("But, just as you started to have fun, your mom says it's time to go home...")
            time.sleep(1.5)
            print("Goodbye")
        if direction == "right":
            time.sleep(1.5)
            print("As you start to spin to the right, a squeaky wheel begins to squeak")
            time.sleep(1.5)
            print("This causes your ears to bleed and you to go to the hospital.")
            time.sleep(1.5)
            print("[Insert Dark Souls: YOU DIED here]")
        time.sleep(1.5)
        ending = input("GAME OVER, RESTART?:")
        if ending == "Yes":
            time.sleep(1.5)
            print("Too bad, womp womp, you gotta do chores.")
        if ending == "^^vv<><>BA-":
            time.sleep(2)
#NG+2
            print("WELCOME TO MY PLAYGROUND! YES, IT IS AN ACTUAL PLAYGROUND! - NG+2")
            time.sleep(1.5)
            print("Here at the playground, we have many fun things!")
            time.sleep(1.5)
            print(
                "We have a 'Metal Slide', 'Swing Set', and 'Merry-Go-Round'. Or you could go 'Home'")
            print(
                "(to go to the location where you want to go to, type it EXACTLY as you see it between the two [']'s ['example'])")
            time.sleep(1.5)
            while True:
                location = input("Where do you want to go?:")
                if location == "Metal Slide":
                    time.sleep(1.5)
                    print("Sorry, they were removed for kids losing their entire back from 427th degree burns.")
                if location == "Swing Set":
                    time.sleep(1.5)
                    print(
                        "Well, there is a swing open, but it's the 'bad swing'. Maybe something else would be more fun.")
                if location == "Home":
                    time.sleep(1.5)
                    print("you cant go home.")
                if location == "example":
                    time.sleep(1.5)
                    print("^^vv<><>BA-")
                if location == "Merry-Go-Round":
                    time.sleep(1.5)
                    print("Good choice!")
                    break
            time.sleep(1.5)
            print("Now comes an important question. Spin left or go right?")
            direction = input("Go ")
            if direction == "left":
                time.sleep(1.5)
                print("Alright, then start spinning left!")
                time.sleep(1.5)
                print("As you spin left, you go faster and faster, even without another master!")
                time.sleep(1.5)
                print("But, just as you started to have fun, your mom says it's time to go home...")
                time.sleep(1.5)
                print("Goodbye")
            if direction == "right":
                time.sleep(1.5)
                print("As you start to spin to the right, a squeaky wheel begins to squeak")
                time.sleep(1.5)
                print("This causes your ears to bleed and you to go to the hospital.")
                time.sleep(1.5)
                print("[Insert Dark Souls: YOU DIED here]")
            time.sleep(1.5)
            ending = input("GAME OVER, RESTART?:")
            if ending == "Yes":
                time.sleep(1.5)
                print("Too bad, womp womp, you gotta do chores.")
            if ending == "^^vv<><>BA-":
                time.sleep(2)
#NG+3
                print("WELCOME TO MY PLAYGROUND! YES, IT IS AN ACTUAL PLAYGROUND! - NG+3")
                time.sleep(1.5)
                print("Here at the playground, we have many fun things!")
                time.sleep(1.5)
                print(
                    "We have the: 'Monkey Bars', 'Metal Slide', 'Swing Set', and 'Merry-Go-Round'. Or you could go 'Home'")
                print(
                    "(to go to the location where you want to go to, type it EXACTLY as you see it between the two [']'s ['example'])")
                time.sleep(1.5)
                while True:
                    location = input("Where do you want to go?:")
                    if location == "Monkey Bars":
                        time.sleep(1.5)
                        print("Sorry, they were removed for some stupid kids breaking 3 ribs on them.")
                    if location == "Metal Slide":
                        time.sleep(1.5)
                        print("Sorry, they were removed for kids losing their entire back from 427th degree burns.")
                    if location == "Swing Set":
                        time.sleep(1.5)
                        print(
                            "Well, there is a swing open, but it's the 'bad swing'. Maybe something else would be more fun.")
                    if location == "Home":
                        time.sleep(1.5)
                        print("you cant go home.")
                    if location == "example":
                        time.sleep(1.5)
                        print("^^vv<><>BA-")
                    if location == "Merry-Go-Round":
                        time.sleep(1.5)
                        print("Good choice!")
                        break
                time.sleep(1.5)
                print("Now comes an important question. Spin left or go right?")
                direction = input("Go ")
                if direction == "left":
                    time.sleep(1.5)
                    print("Alright, then start spinning left!")
                    time.sleep(1.5)
                    print("As you spin left, you go faster and faster, even without another master!")
                    time.sleep(1.5)
                    print("But, just as you started to have fun, your mom says it's time to go home...")
                    time.sleep(1.5)
                    print("Goodbye")
                if direction == "right":
                    time.sleep(1.5)
                    print("As you start to spin to the right, a squeaky wheel begins to squeak")
                    time.sleep(1.5)
                    print("This causes your ears to bleed and you to go to the hospital.")
                    time.sleep(1.5)
                    print("[Insert Dark Souls: YOU DIED here]")
                time.sleep(1.5)
                ending = input("GAME OVER, RESTART?:")
                if ending == "Yes":
                    time.sleep(1.5)
                    print("Too bad, womp womp, you gotta do chores.")
                if ending == "^^vv<><>BA-":
                    time.sleep(2)
#NG+4
                    print("WELCOME TO MY PLAYGROUND! YES, IT IS AN ACTUAL PLAYGROUND! - 'NG+4'")
                    time.sleep(1.5)
                    print("Here at the playground, we have many fun things!")
                    time.sleep(1.5)
                    print(
                        "We have the: 'Monkey Bars', 'Metal Slide', 'Swing Set', and 'Merry-Go-Round'. Or you could go 'Home'")
                    print(
                        "(to go to the location where you want to go to, type it EXACTLY as you see it between the two [']'s ['example'])")
                    time.sleep(1.5)
                    while True:
                        location = input("Where do you want to go?:")
                        if location == "Monkey Bars":
                            time.sleep(1.5)
                            print("Sorry, they were removed for some stupid kids breaking 3 ribs on them.")
                        if location == "Metal Slide":
                            time.sleep(1.5)
                            print("Sorry, they were removed for kids losing their entire back from 427th degree burns.")
                        if location == "Swing Set":
                            time.sleep(1.5)
                            print(
                                "Well, there is a swing open, but it's the 'bad swing'. Maybe something else would be more fun.")
                        if location == "Home":
                            time.sleep(1.5)
                            print("you cant go home.")
                        if location == "example":
                            time.sleep(1.5)
                            print("^^vv<><>BA-")
                        if location == "NG+4":
                            time.sleep(1.5)
                            print("'Alone! Infection! Void! S**t attacking from the other side, yuck! Alone! Infection! Chaos! A-B-C-D-E-F, go! Checkmate (checkmate), informed consent (oh, yeah). It increases words. Relation (relation). Duration (oh, yeah). Build and realize. MESSIAH! Will not come. Parallax! Paradox! Paradigm will attack! We've got only one sky! Blue, red, and black paranoia. What is it like to you? No one can see the colors but you! Alone! Infection! Void! S**t attacking from the other side yuck! Alone! Infection! Chaos! A-B-C-D-E-F, go! Light and darkness invisible (oh, yeah). Your soul dissipates. Destruction  re-reduction (oh, yeah). TOWER OF BABEL! MESSIAH! Will not come. Parallax! Paradox! Paradigm will attack! We've got only one sky! Blue, red, and black paranoia. What is it like to you? No one can see the colors but you! ...I had to run away from here...Before the storm hit...We see eye to eye...We see eye to eye...I told me, without you! We've got only one sky! Blue, red, and black (BLUE, RED, AND BLACK) paranoia (paranoia)! What is it like to you? (LIKE TO YOU!) No one can see the colors but you! We've got only one sky! Joy, grief, and fun PARANOIA! What is it like to you? No one can see the colors, the colors, but you!'")

                        if location == "Merry-Go-Round":
                            time.sleep(1.5)
                            print("Good choice!")
                            break
                    time.sleep(1.5)
                    print("Now comes an important question. Spin left or go right?")
                    direction = input("Go ")
                    if direction == "left":
                        time.sleep(1.5)
                        print("Alright, then start spinning left!")
                        time.sleep(1.5)
                        print("As you spin left, you go faster and faster, even without another master!")
                        time.sleep(1.5)
                        print("But, just as you started to have fun, your mom says it's time to go home...")
                        time.sleep(1.5)
                        print("Goodbye")
                    if direction == "right":
                        time.sleep(1.5)
                        print("As you start to spin to the right, a squeaky wheel begins to squeak")
                        time.sleep(1.5)
                        print("This causes your ears to bleed and you to go to the hospital.")
                        time.sleep(1.5)
                        print("[Insert Dark Souls: YOU DIED here]")
                    time.sleep(1.5)
                    ending = input("GAME OVER, RESTART?:")
                    if ending == "Yes":
                        time.sleep(1.5)
                        print("Too bad, womp womp, you gotta do chores.")
                    if ending == "^^vv<><>BA-":
                        time.sleep(1.5)
                        print("Sorry, that won't work anymore...")
                        time.sleep(1.5)
                        print("Now, you will listen to my favorite song, Alone Infection, ON LOOP FOR ETERNITY!")
                    if ending == "Alone! Infection! Void! S**t attacking from the other side, yuck! Alone! Infection! Chaos! A-B-C-D-E-F, go! Checkmate (checkmate), informed consent (oh, yeah). It increases words. Relation (relation). Duration (oh, yeah). Build and realize. MESSIAH! Will not come. Parallax! Paradox! Paradigm will attack! We've got only one sky! Blue, red, and black paranoia. What is it like to you? No one can see the colors but you! Alone! Infection! Void! S**t attacking from the other side yuck! Alone! Infection! Chaos! A-B-C-D-E-F, go! Light and darkness invisible (oh, yeah). Your soul dissipates. Destruction  re-reduction (oh, yeah). TOWER OF BABEL! MESSIAH! Will not come. Parallax! Paradox! Paradigm will attack! We've got only one sky! Blue, red, and black paranoia. What is it like to you? No one can see the colors but you! ...I had to run away from here...Before the storm hit...We see eye to eye...We see eye to eye...I told me, without you! We've got only one sky! Blue, red, and black (BLUE, RED, AND BLACK) paranoia (paranoia)! What is it like to you? (LIKE TO YOU!) No one can see the colors but you! We've got only one sky! Joy, grief, and fun PARANOIA! What is it like to you? No one can see the colors, the colors, but you!":
                        time.sleep(1.5)
                        print("Oh, you like this song too? GREAT! You can go home now.")
                        time.sleep(1.5)
                        print("CONGRATULATIONS, YOU WIN!!!!!")
"""