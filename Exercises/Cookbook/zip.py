prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# sort the dict by the values
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))


# NOTICE
# zip() created a generator could be used once
#
# prices_and_names = zip(prices.values(), price.keys())
# print(min(prices_and_names)) is OK
# print(max(prices_and_names)) will throw a ValueError: max() arg is an empty
# sequence
#
# With zip, keys will dominate when values are the same
