numbers = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, numbers)))

nums = [10, 15, 20]
print(list(filter(lambda x: x > 12, nums)))

data = [3, 6, 9]
print(list(filter(lambda x: x > 5, data)))

values = [7, 8, 9]
print(list(filter(lambda x: x != 8, values)))
