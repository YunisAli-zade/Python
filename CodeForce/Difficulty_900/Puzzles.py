def puzzles() -> int:
    n, m = map(int, input().split())
    puzzels_in_the_shop = list(map(int, input().split()))
    puzzels_in_the_shop.sort()
    return max(puzzels_in_the_shop[:n - 1]) - min(puzzels_in_the_shop[:n - 1])
print(puzzles())