# Xom Data · Second largest value
# Problem: https://xomdata.com/practice/py-second-largest
# Solved: 2026-10-20

def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first_largest = max(numbers)
    second_largest = None
    for number in numbers:
        if number != first_largest:
            if second_largest is None or number > second_largest:
                second_largest = number
    return second_largest
