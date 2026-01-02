def chat_room() -> str:
    word = input().strip()
    target = "hello"
    j = 0
    for char in word:
        if j < len(target) and char == target[j]:
            j += 1
    return "YES" if j == len(target) else "NO"
print(78/2)