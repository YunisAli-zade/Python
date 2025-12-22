def soldier_and_bananas() -> int:
    s = 0
    collection = list(map(int, input().split()))
    k = collection[0]
    n = collection[1]
    w = collection[2]
    for  i in range(1, w + 1):
        s += i * k
    return 0 if s <= n else s - n
print(soldier_and_bananas())