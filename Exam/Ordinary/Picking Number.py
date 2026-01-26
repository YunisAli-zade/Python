from collections import Counter
def solution(a: list[int]) -> int:
    dic = Counter(a)
    if len(dic) == 1:
        return dic[a[0]]
    max_len_subarr = 0
    for num in a:
        max_len_subarr = max(max_len_subarr, dic[num] + dic.get(num + 1, 0))
    return max_len_subarr
    pass
print(solution([9, 29, 21, 96, 63, 85]))