from collections import Counter
def solution(arr: list[int], brr: list[int]) -> list[int]:
    dictt_arr = Counter(arr)
    dictt_brr = Counter(brr)
    missing = []
    for el in dictt_brr:
        if dictt_brr[el] > dictt_arr.get(el, 0):
            missing.append(el)
    return sorted(missing)
    pass
arr=[203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr=[203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
print(solution(arr, brr))