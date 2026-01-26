def solution(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    for i in range(len(flowerbed)):
        prev =  i - 1 if i - 1 >= 0 else i
        next = i + 1 if i + 1 < len(flowerbed) else i
        if flowerbed[i] == 0 and flowerbed[prev] == 0 and flowerbed[next] == 0:
            flowerbed[i] = 1
            n -= 1
    return True if n == 0 else False
    pass
# print(solution([1,0,0,0,1], 1))