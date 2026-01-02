from collections import Counter
def solution(nums: list[int], target: int) -> bool:
    l = len(nums) // 2
    nums = Counter(nums)
    for el in nums:
        if el == target:
            return True if nums[el] > l else False
    pass