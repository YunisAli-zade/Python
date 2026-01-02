def can_solve_problem() -> int:
    n = int(input())
    count = 0
    for i in range(n):
        arr = list(map(int, input().split()))
        if sum(arr) >= 2:
            count += 1
    return count
print(can_solve_problem())