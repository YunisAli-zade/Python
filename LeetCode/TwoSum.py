def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    i = 0
    for num in nums:
        if num not in dic:
            dic[num] = i
        else:
            dic[num] = i
        i += 1
    for j in range(len(nums)):
        if target - nums[j] in dic:
            if dic[target - nums[j]] != j:
                return [j, dic[target - nums[j]]]
# Time O(n where n id the length of nums). In practice: O(2 * n)
# Space O(k where k is the length of dic)