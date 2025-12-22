def enters_to_the_next_round() -> int:
    n, k = map(int, input().split())
    result = 0
    scores = list(map(int, input().split()))
    for score in scores:
        if score >= scores[k-1] and score > 0:
            result += 1
    return result
print(enters_to_the_next_round())