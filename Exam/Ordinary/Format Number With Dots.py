def solution(n: int) -> str:
    n = str(n)[::-1]
    parts = [n[i:i + 3] for i in range(0, len(n), 3)]
    s = '.'.join(parts)
    return s[::-1]
    pass