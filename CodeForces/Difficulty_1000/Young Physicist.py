def young_phisicist() -> str:
    n = int(input())
    summ_x = 0
    summ_y = 0
    summ_z = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        summ_x += x
        summ_y += y
        summ_z += z
    if summ_x == 0 and summ_y == 0 and summ_z == 0:
        return "YES"
    else:
        return "NO"
print(young_phisicist())