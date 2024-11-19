players = int(input("How many players are playing?: "))
p1_rating = int()
p2_rating = int()
p3_rating = int()
p4_rating = int()
p5_rating = int()

if players >= 1 and players <= 5:
    p1_rating = int(input("Player 1, how would you rate this model from 1-5?: "))
    print("You give them a:", p1_rating)
    if players >=2:
        p2_rating = int(input("Player 2, how would you rate this model from 1-5?: "))
        print("You give them a:", p2_rating)
        if players >= 3:
            p3_rating = int(input("Player 3, how would you rate this model from 1-5?: "))
            print("You give them a:", p3_rating)
            if players >= 4:
                p4_rating = int(input("Player 4, how would you rate this model from 1-5?: "))
                print("You give them a:", p4_rating)
                if players == 5:
                    p5_rating = int(input("Player 5, how would you rate this model from 1-5?: "))
                    print("You give them a:", p5_rating)
elif players < 1:
    print("Sorry, not enough players")
elif players > 5:
    print("Sorry, too many players")

if players >= 1 and players <= 5:
    print("Now, for the average score!")
    ratesum = p1_rating + p2_rating + p3_rating + p4_rating + p5_rating
    averate = ratesum/players
    print(averate)
