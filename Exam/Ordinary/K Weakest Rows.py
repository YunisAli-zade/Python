def solution(mat, k):
    strengths = []
    
    for i, row in enumerate(mat):
        # Count leading 1s (soldiers)
        count = 0
        for val in row:
            if val == 1:
                count += 1
            else:
                break
        strengths.append((count, i))
    
    # Sort by (strength, index)
    strengths.sort(key=lambda x: (x[0], x[1]))
    
    # Return first k indices
    return [idx for _, idx in strengths[:k]]
	pass