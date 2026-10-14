# Xom Data · Count vowels in a name
# Problem: https://xomdata.com/practice/py-vowels
# Solved: 2026-10-14

def count_vowels(name):
    return sum(1 for char in name.lower() if char in "aeiou")
