# Xom Data · Merge intervals
# Problem: https://xomdata.com/practice/py-merge-intervals
# Solved: 2026-10-24

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])
    result = [intervals[0][:]]

    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])

    return result
