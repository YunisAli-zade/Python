from collections import Counter
def solution(s: str) -> str:
	stack = []
	for char in s:
		if stack and stack[-1] == char:
			stack.pop()  # Remove pair
		else:
			stack.append(char)
	return ''.join(stack) or "Empty String"
    pass