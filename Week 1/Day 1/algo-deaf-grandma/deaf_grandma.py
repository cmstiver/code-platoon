def deaf_grandma():
    print("HEY KID!")
    goodbyeCounter = 0
    while True:
        answer = input("> ")
        if answer == "GOODBYE!":
            goodbyeCounter += 1
            if goodbyeCounter >= 2:
                print("LATER, SKATER!")
                break
            print("LEAVING SO SOON?")
        elif answer.upper() != answer:
            print("SPEAK UP, KID!")
            goodbyeCounter = 0
        else:
            print("NO, NOT SINCE 1946!")
            goodbyeCounter = 0


deaf_grandma()