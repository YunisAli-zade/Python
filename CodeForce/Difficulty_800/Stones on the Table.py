def stones_on_the_table() -> int:
    n = int(input())
    s = input()
    result = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            result += 1
    return result
print(stones_on_the_table())