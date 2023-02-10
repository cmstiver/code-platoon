def char_count(str):
    str = str.replace(" ", "")
    str = sorted(str)
    dictCounter = {}
    for x in str:
        if x in dictCounter:
            dictCounter[x] += 1
        else:
            dictCounter[x] = 1
    dictCounter = dict(
        sorted(dictCounter.items(), key=lambda x: x[1], reverse=True))
    keys = dictCounter.keys()
    values = dictCounter.values()
    zipList = list(map(list, zip(keys, values)))

    return zipList
