def factorial(num):
    total = num

    for x in range(total - 1, 0, -1):
        total *= x

    return total


print(factorial(4))
