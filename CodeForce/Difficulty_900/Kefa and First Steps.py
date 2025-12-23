def kefa_and_first_steps() -> int:
    n = int(input())
    subseqment = list(map(int, input().split()))
    count = 1
    largest_subseqment = 1
    for i in range(1, n):
        if subseqment[i - 1] <= subseqment[i]:
            count += 1
            largest_subseqment = max(largest_subseqment, count)
        else:
            count = 1
    return largest_subseqment
print(kefa_and_first_steps())