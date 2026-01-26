from collections import Counter
a = "aabbcc"
a = Counter(a)
arr = []
for char in a.values():
    arr.append(char)
for i in range(len(arr)):
    