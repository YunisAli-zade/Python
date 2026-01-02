def twins() -> int:
    n = int(input())
    coins = list(map(int, input().split()))
    coins = sorted(coins, reverse = True)
    taken = 0
    total = sum(coins)
    count = 0
    for coin in coins:
        taken += coin
        count += 1
        if taken > total - taken:
            break
    return count
print(twins())