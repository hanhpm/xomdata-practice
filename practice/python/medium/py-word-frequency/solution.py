# Xom Data · Word frequency count in text
# Problem: https://xomdata.com/practice/py-word-frequency
# Solved: 2026-10-16

def word_frequency(text):
    count_term = {}
    words = text.split()

    for word in words:
        if word in count_term:
            count_term[word] += 1
        else:
            count_term[word] = 1
    return count_term
