
def translateWord(word):
    vowelList = ["a", "e", "i", "o", "u"]
    tracker = []
    result = ""
    punctuation = ""
    consonants = ""

    if word[0] in vowelList:
        result = word
    else:
        vowelHit = False
        for x in word:
            if x.isalpha():
                if x == x.upper():
                    tracker.append("upper")
                elif x == x.lower():
                    tracker.append("lower")
            else:
                punctuation += x
                continue

            x = x.lower()

            if x not in vowelList and not vowelHit:
                consonants += x
            else:
                if consonants[-1] == "q" and x == "u":
                    consonants += x
                    continue
                vowelHit = True
                result += x

        result = list(result)
        for i in range(len(tracker) - 1):
            if tracker[i] == "upper":
                result[i] = result[i].upper()
        result = "".join(result)

        result += consonants

    print(tracker)

    result += "ay"
    result += punctuation

    return result


def translate(phrase):
    phrase = phrase.split(" ")

    phrase = list(map(lambda word: translateWord(word), phrase))

    result = " ".join(phrase)

    return result


print(translate("Hello World!"))  # Ellohay Orldway!
