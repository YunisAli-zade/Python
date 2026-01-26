def getFinalOpenedDoors():
    arr = [1] * 100
    ans = []
    n = len(arr)
    step = 1
    while step <= n:
        current_el = step - 1
        while current_el < n:
            arr[current_el] = 1 if arr[current_el] == 0 else 0
            current_el += step
        step += 1
    
    for i, state in enumerate(arr):
        if state == 0:
            ans.append(i + 1)
    return ans
print(getFinalOpenedDoors())