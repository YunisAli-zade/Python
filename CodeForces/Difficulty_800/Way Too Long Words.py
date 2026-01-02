def long_words():
    n = int(input())
    for i in range(n):
        word = input()
        if len(word) > 10:
            temp = len(word) - 2
            print(word[0] + str(temp) + word[-1])
        else:
            print(word)
long_words()