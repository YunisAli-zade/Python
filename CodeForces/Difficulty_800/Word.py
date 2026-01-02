def word() -> str:
    Word = input()
    low_lett = 0
    up_lett = 0
    for char in Word:
        if char.islower():
            low_lett += 1
        if char.isupper():
            up_lett += 1
    return Word.lower() if low_lett >= up_lett else Word.upper()
print(word())