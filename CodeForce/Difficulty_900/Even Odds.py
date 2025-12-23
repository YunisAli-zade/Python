def even_odds() -> list:
    n, k = map(int, input().split())
    odd_count = (n + 1) // 2
    if k <= odd_count:
        return 2 * k - 1
    else:
        return 2 * (k - odd_count)
print(even_odds())