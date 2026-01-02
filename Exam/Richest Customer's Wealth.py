def solution(accounts: list[list[int]]) -> int:
    max_wealth = 0
    for account in accounts:
        max_wealth = max(sum(account), max_wealth)
    return max_wealth
    pass