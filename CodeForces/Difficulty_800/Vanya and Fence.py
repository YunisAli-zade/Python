def vanya_and_fence() -> int:
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    row_width = 0
    for i in range(n):
        if arr[i] > h:
            row_width += 2
        else:
            row_width += 1
    return row_width
print(vanya_and_fence())