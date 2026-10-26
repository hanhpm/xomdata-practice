# Xom Data · Climbing stairs
# Problem: https://xomdata.com/practice/py-climb-stairs
# Solved: 2026-10-26

def climb_stairs(n):
    if n <= 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b
