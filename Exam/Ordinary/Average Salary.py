def solution(salary: list[int]) -> float:
    n = len(salary)
    sum = 0
    salary = sorted(salary)
    for i in range(1, n - 1):
        sum += salary[i]
    average_salary = sum / (n - 2)
    return average_salary
    pass
