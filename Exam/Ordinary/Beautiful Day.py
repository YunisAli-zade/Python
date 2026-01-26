def solution(i: int, j: int, k: int) -> int:
    def reverse_digit(n):
        n = abs(n)
        newn = 0
        while n > 0:
            digit = n % 10
            newn = newn * 10 + digit
            n //= 10
        return newn
    count = 0
    for d in range(i, j + 1):
        if abs(reverse_digit(d) - d) % k == 0:
            count += 1
    return count
    pass
print(solution(20, 23, 6))