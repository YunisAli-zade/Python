from collections import Counter
def anton_and_danik() -> str:
    n = int(input())
    s = input()
    sett = Counter(s)
    anton = sett["A"]
    danik = sett["D"]
    if anton > danik:
        return "Anton"
    elif danik > anton:
        return "Danik"
    else:
        return "Friendship"
print(anton_and_danik())