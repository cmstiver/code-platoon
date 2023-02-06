def deaf_grandma():
    goodbye = False
    print("HEY KID!")
    while goodbye == False:
        answer = input("> ")
        if answer == "GOODBYE!":
            print("LEAVING SO SOON?")
            goodbyeAnswer = input("> ")
            if goodbyeAnswer == "GOODBYE!":
                print("LATER, SKATER!")
                break
        if answer.upper() != answer:
            print("SPEAK UP, KID!")
        else:
            print("NO, NOT SINCE 1946!")




deaf_grandma()