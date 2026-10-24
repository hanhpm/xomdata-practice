# Xom Data · Valid nested parentheses
# Problem: https://xomdata.com/practice/py-valid-brackets
# Solved: 2026-10-24

def is_valid(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0
