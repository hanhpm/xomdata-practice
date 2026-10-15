# Xom Data · Check palindrome
# Problem: https://xomdata.com/practice/py-palindrome
# Solved: 2026-10-15

def is_palindrome(text):
    pointer1 = 0
    pointer2 = len(text) - 1
    while pointer1 < pointer2:
        if text[pointer1].lower() != text[pointer2].lower():
            return False

        pointer1 += 1
        pointer2 -= 1

    return True
