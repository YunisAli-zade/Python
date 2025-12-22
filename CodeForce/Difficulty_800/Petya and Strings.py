def petya_and_strings() -> str:
    word1 = input()
    word2 = input()
    word1 = word1.lower()
    word2 = word2.lower()
    if word1 > word2:
        return("1")
    elif word1 < word2:
        return("-1")
    else:
        return("0")
    return "Error, couldn't find the answer."
print(petya_and_strings())