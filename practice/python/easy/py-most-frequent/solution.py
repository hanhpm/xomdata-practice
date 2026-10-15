# Xom Data · Most frequent character
# Problem: https://xomdata.com/practice/py-most-frequent
# Solved: 2026-10-15

def most_frequent(text):
    freq = {}

    for char in text.lower():
        freq[char] = freq.get(char,0) + 1
    max_char = None
    max_count = 0

    for char,count in freq.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_char
