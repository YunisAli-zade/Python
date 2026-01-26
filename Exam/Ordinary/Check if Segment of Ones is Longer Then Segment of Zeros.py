def solution(s: str) -> bool:
    max_c_1 = 0
    max_c_0 = 0
    curr_1 = 0
    curr_0 = 0
    for c in s:
        if c == "1":
            curr_1 += 1
            curr_0 = 0
        else:
            curr_1 = 0
            curr_0 += 1
        max_c_1 = max(curr_1, max_c_1)
        max_c_0 = max(curr_0, max_c_0)
    return True if max_c_1 > max_c_0 else False
    pass
