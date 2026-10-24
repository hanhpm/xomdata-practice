# Xom Data · Longest substring without repeating characters
# Problem: https://xomdata.com/practice/py-longest-unique-substring
# Solved: 2026-10-24

def longest_unique(s):
    positions = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in positions and positions[char] >= left:
            left = positions[char] + 1

        positions[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
