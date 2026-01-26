def solution(a: list[int]) -> int:
    dic = dict()
    min_distance = float('inf')
    for i in range(len(a)):
        if a[i] in dic:
            min_distance = min(min_distance, abs(dic[a[i]] - i))
        else:
            dic[a[i]] = i
    return -1 if min_distance == float('inf') else min_distance
    pass
