def boy_or_girl() -> str:
    word = input()
    s = set(word)
    length = len(s)
    return "CHAT WITH HER!" if length % 2 == 0 else "IGNORE HIM!"
print(boy_or_girl())