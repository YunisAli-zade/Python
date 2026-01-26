def solution(arr: list[int]) -> list[int]:
    memo = sorted(list(set(arr)))
    dic = {}
    ans = []
    for i in range(len(memo)):
        dic[memo[i]] = i + 1
    for num in arr:
        temp = dic[num]
        ans.append(temp)
    return ans
    pass
print(solution([40, 10, 20, 30]))