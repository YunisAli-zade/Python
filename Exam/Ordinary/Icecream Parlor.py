def solution(m: int, cost: list[int]) -> list[int]:
    seen = {}
    for i, v in enumerate(cost, 1):
        need = m - v
        if need in seen:
            a = seen[need]
            b = i
            return [a, b] if a < b else [b, a]
        seen[v] = i
    return []

print(solution(6, [1, 2, 3, 4, 5]))