def nearly_lucky_number() -> str:
    lucky = {4, 7}
    n = int(input())
    count = 0
    while n > 0:
        digit = n % 10
        if digit in lucky:
            count += 1
        n //= 10
    return "YES" if count in lucky else "NO"
print(nearly_lucky_number())