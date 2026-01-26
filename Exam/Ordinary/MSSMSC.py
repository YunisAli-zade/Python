def solution(nums: list[int], queries: list[int]) -> list[int]:
    ans = []
    nums.sort()
    for queue in queries:
        sum = 0
        count = 0
        for num in nums:
            if sum + num > queue:
                break
            else:
                sum += num
                count += 1
        ans.append(count)
    return ans
    pass
