def bottles(num):
    bottlesLeft = num
    start = num
    while bottlesLeft != 0:
        if (bottles == 1):
            print(
                f"{bottlesLeft} bottle of beer on the wall, {bottlesLeft} bottle of beer.")
        else:
            print(
                f"{bottlesLeft} bottles of beer on the wall, {bottlesLeft} bottles of beer.")

        bottlesLeft -= 1

        if (bottlesLeft == 0):
            print(
                "Take one down and pass it around, no more bottles of beer on the wall.")
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print(
                f"Go to the store and buy some more, {start} bottles of beer on the wall.")
        else:
            print(
                f"Take one down and pass it around, {bottlesLeft} bottles of beer on the wall.")


bottles(99)
