def helpful_maths() -> str:
    equation = input()
    numbers = equation.split('+')
    numbers = [int(num) for num in numbers]
    numbers.sort()
    sorted_equation = '+'.join(str(num) for num in numbers)
    return sorted_equation
print(helpful_maths())