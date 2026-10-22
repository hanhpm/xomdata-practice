# Xom Data · Count pairs with a target sum
# Problem: https://xomdata.com/practice/py-two-sum-count
# Solved: 2026-10-22

def count_pairs(numbers, target):
    count = 0
    seen = {}

    for num in numbers:
        complement = target - num

        if complement in seen:
            count += seen[complement]

        seen[num] = seen.get(num, 0) + 1

    return count
