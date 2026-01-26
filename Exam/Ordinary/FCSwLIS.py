def solution(list1: list[str], list2: list[str]) -> list[str]:
    dic = {}
    ans = []
    min_sum_index = float('inf')
    for el in list1:
        dic[el] = list1.index(el)
    for i, el in enumerate(list2):
        if el in dic:
            if i + dic[el] < min_sum_index:
                ans.append(el)
                ans = [ans[-1]]
                min_sum_index = i + dic[el]
            elif i + dic[el] == min_sum_index:
                ans.append(el)
            else:
                continue
    return ans