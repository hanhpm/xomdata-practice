# Xom Data · Best selling products board
# Problem: https://xomdata.com/practice/py-top-n-with-tie
# Solved: 2026-10-21

def top_products(sales, n):
    products = sorted(sales.items(), key=lambda x: (-x[1], x[0]))
    return [name for name, _ in products[:n]]
