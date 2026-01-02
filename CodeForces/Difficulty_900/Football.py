def football() -> str:
    players = input().strip()
    count = 1
    for i in range(1, len(players)):
        if players[i] == players[i-1]:
            count += 1
            if count >= 7:
                return "YES"
        else:
            count = 1
    return "NO"

print(football())