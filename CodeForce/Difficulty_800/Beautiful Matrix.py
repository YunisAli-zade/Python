def beautifull_matrix() -> int:
    coordinate_of_1 = [0, 0]
    for i in range(5):
        row = list(map(int, input().split()))
        for j in range(5):
            if row[j] == 1:
                coordinate_of_1[0], coordinate_of_1[1] = i + 1, j + 1
    return abs(coordinate_of_1[0] - 3) + abs(coordinate_of_1[1] - 3)
print(beautifull_matrix())