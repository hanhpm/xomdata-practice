# Xom Data · Compute price after discount
# Problem: https://xomdata.com/practice/py-discount
# Solved: 2026-10-12

def final_price(price, percent):
    percent_price = price*percent/100
    final_price = price-percent_price
    return round(final_price,2)
