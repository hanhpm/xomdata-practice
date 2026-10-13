# Xom Data · Total receipts
# Problem: https://xomdata.com/practice/py-sum-positive
# Solved: 2026-10-13

def sum_positive(numbers: list[float]) -> float:
    total = 0
    for x in numbers:
        if x > 0:
            total += x
    return total
