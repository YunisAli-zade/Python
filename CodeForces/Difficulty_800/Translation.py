def translation() -> str:
    word1 = input()
    word2 = input()
    isreverse = word1 == word2[::-1]
    return "YES" if isreverse else "NO"
print(translation())