def puzzles() -> int:
    n, m = map(int, input().split())
    puzzels_in_the_shop = list(map(int, input().split()))
    puzzels_in_the_shop.sort()
    current_window = puzzels_in_the_shop[:n]
    min_diff = max(current_window) - min(current_window)
    for i in range(1, m - n + 1):
        current_window = puzzels_in_the_shop[i:i + n]
        current_diff = max(current_window) - min(current_window)
        if current_diff < min_diff:
            min_diff = current_diff
    return min_diff
print(puzzles())