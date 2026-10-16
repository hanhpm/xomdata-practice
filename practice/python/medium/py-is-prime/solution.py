# Xom Data · Check prime number
# Problem: https://xomdata.com/practice/py-is-prime
# Solved: 2026-10-16

def is_prime(n):
    # if n >= 2 and n % 1 and n % n:
    #     return True
    # else:
    #     return False
    # return is_prime
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
