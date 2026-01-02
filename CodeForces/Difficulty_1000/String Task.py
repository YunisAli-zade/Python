def string_task() -> str:
    sett = {"A", "O", "Y", "E", "U", "I"}
    s = list(input())
    s = [char for char in s if char.upper() not in sett]
    return "".join(["." + char.lower() for char in s])
print(string_task())