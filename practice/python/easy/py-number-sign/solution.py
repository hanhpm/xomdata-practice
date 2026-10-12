# Xom Data · Determine the sign of a number
# Problem: https://xomdata.com/practice/py-number-sign
# Solved: 2026-10-12

def number_sign(n):
    input = n
    if n>0:
        return("1")
    elif n<0:
        return("-1")
    else:
        return("0")
    return number_sign(n)
