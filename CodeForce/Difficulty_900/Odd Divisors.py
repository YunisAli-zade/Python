def odd_divisor() -> list:
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        while n % 2 == 0:
            n //= 2
        if n > 1:
            result.append("YES")
        else:
            result.append("NO")
    for conclusion in result:
        print(conclusion, end = "\n")
    return result
odd_divisor()