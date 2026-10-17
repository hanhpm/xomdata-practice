# Xom Data · Group products by category
# Problem: https://xomdata.com/practice/py-group-category
# Solved: 2026-10-17

def group_by_category(items):
    result = {}

    for product, category in items:
        if category not in result:
            result[category] = []

        result[category].append(product)

    return result
