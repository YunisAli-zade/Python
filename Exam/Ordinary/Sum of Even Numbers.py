def solution(nums: list[int]) -> int:
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum
    pass
