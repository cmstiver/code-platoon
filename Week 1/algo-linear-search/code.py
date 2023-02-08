array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)


def linear_search(value_to_find, array_to_search_through):
    for i in range(len(array_to_search_through)):
        if (array_to_search_through[i] == value_to_find):
            return i


def linear_search_global(value_to_find, array_to_search_through):
    arr = []
    for i in range(len(array_to_search_through)):
        if (array_to_search_through[i] == value_to_find):
            arr.append(i)
    return arr
