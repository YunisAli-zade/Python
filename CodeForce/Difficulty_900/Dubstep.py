def dubstep() -> str:
    s = input()
    arr = s.split(sep = "WUB")
    words = [word for word in arr if word != '']
    return " ".join(words)
print(dubstep())