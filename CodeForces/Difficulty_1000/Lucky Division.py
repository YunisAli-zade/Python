def lucky_division() -> str:
    n = input()
    int_n = int(n)
    def find_lucky(x: int) -> bool:
        target = {"4", "7"}
        lucky = True
        x = str(x)
        for digit in x:
            if digit not in target:
                lucky = False
                break
        if lucky:
            return True
        else:
            return False
    for i in range(1, int_n + 1):
        if find_lucky(i) and int_n % i == 0:
            return "YES"
    return "NO"
print(lucky_division())