# Xom Data · Maximum subarray sum
# Problem: https://xomdata.com/practice/py-max-subarray
# Solved: 2026-10-24

def max_subarray(numbers):
    current_sum = numbers[0]
    max_sum = numbers[0]

    for num in numbers[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
