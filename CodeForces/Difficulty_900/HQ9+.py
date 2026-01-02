def hq9p() -> str:
    sett = {"H", "Q", "9"}
    p = input()
    for char in p:
        if char in sett:
            return "YES"
    return "NO"
print(hq9p())