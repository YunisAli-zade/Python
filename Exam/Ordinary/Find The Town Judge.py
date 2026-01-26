def solution(n: int, trust: list[list[int]]) -> int:
    dic = {}
    for i in range(1, n + 1):
        dic[i] = 0
    for p in trust:
        temp = p[0]
        dic[temp] = p[1]
    for j in range(1, n + 1):
        if dic[j] == 0:
            return j
    return -1
    pass
print(solution(3, [[1, 2], [2, 3]]))