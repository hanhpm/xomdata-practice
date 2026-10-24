# Xom Data · Two sum
# Problem: https://xomdata.com/practice/py-two-sum-indices
# Solved: 2026-10-24

def two_sum(numbers, target):
    positions = {}
    result = []

    for i in range(len(numbers) - 1, -1, -1):
        complement = target - numbers[i]

        if complement in positions:
            result = [i, positions[complement]]

        positions[numbers[i]] = i

    return result
