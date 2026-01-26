from collections import Counter
def solution(nums: list[int]) -> int:
    c = Counter(nums)
    return sum(num for num in c if c[num] == 1)
    pass
