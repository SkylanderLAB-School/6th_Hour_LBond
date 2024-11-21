players = int(input("How many players are playing?: "))
p1_rating = int()
p2_rating = int()
p3_rating = int()
p4_rating = int()
p5_rating = int()
p6_rating = int()
p7_rating = int()
p8_rating = int()
p9_rating = int()
p10_rating = int()
p11_rating = int()
p12_rating = int()
p13_rating = int()
p14_rating = int()
p15_rating = int()
p16_rating = int()

if players >= 1 and players <= 16:
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
                if players >= 5:
                    p5_rating = int(input("Player 5, how would you rate this model from 1-5?: "))
                    print("You give them a:", p5_rating)
                    if players >= 6:
                        p6_rating = int(input("Player 6, how would you rate this model from 1-5?: "))
                        print("You give them a:", p6_rating)
                        if players >= 7:
                            p7_rating = int(input("Player 7, how would you rate this model from 1-5?: "))
                            print("You give them a:", p7_rating)
                            if players >= 8:
                                p8_rating = int(input("Player 8, how would you rate this model from 1-5?: "))
                                print("You give them a:", p8_rating)
                                if players >= 9:
                                    p9_rating = int(input("Player 9, how would you rate this model from 1-5?: "))
                                    print("You give them a:", p9_rating)
                                    if players >= 10:
                                        p10_rating = int(input("Player 10, how would you rate this model from 1-5?: "))
                                        print("You give them a:", p10_rating)
                                        if players >= 11:
                                            p11_rating = int(input("Player 11, how would you rate this model from 1-5?: "))
                                            print("You give them a:", p11_rating)
                                            if players >= 12:
                                                p12_rating = int(input("Player 12, how would you rate this model from 1-5?: "))
                                                print("You give them a:", p12_rating)
                                                if players >= 13:
                                                    p13_rating = int(input("Player 13, how would you rate this model from 1-5?: "))
                                                    print("You give them a:", p13_rating)
                                                    if players >= 14:
                                                        p14_rating = int(input("Player 14, how would you rate this model from 1-5?: "))
                                                        print("You give them a:", p14_rating)
                                                        if players >= 15:
                                                            p15_rating = int(input("Player 15, how would you rate this model from 1-5?: "))
                                                            print("You give them a:", p15_rating)
                                                            if players == 16:
                                                                p16_rating = int(input("Player 16, how would you rate this model from 1-5?: "))
                                                                print("You give them a:", p16_rating)
elif players < 1:
    print("Sorry, not enough players")
elif players > 16:
    print("Sorry, too many players")

if players >= 1 and players <= 16:
    print("Now, for the average score!")
    ratesum = p1_rating + p2_rating + p3_rating + p4_rating + p5_rating + p6_rating + p7_rating + p8_rating + p9_rating + p10_rating + p11_rating + p12_rating + p13_rating + p14_rating + p15_rating + p16_rating
    averate = ratesum/players
    print(averate)
