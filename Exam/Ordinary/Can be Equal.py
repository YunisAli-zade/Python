from collections import Counter
def solution(target: list[int], arr: list[int]) -> bool:
    return Counter(target) == Counter(arr)
    pass
