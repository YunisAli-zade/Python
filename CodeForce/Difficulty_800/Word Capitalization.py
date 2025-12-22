def word_capitalization() -> str:
    word = input()
    return word[0].upper() + word[1:]
print(word_capitalization())