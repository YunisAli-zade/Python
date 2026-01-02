def bit_pp() -> int:
    n = int(input())
    result = 0
    for i in range(n):
        op = input()
        if op == "X++" or op == "++X":
            result += 1
        if op == "X--" or op == "--X":
            result -= 1
    return result
print(bit_pp())