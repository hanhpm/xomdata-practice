# Xom Data · Sentence segmentation with a dictionary
# Problem: https://xomdata.com/practice/py-word-break
# Solved: 2026-10-26

def word_break(s, words):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for word in words:
            start = i - len(word)

            if start >= 0 and dp[start] and s.startswith(word, start):
                dp[i] = True
                break

    return dp[n]
