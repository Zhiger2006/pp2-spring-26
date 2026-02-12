numbers = [5, 2, 9, 1]
print(sorted(numbers, key=lambda x: x))

words = ["apple", "kiwi", "banana"]
print(sorted(words, key=lambda x: len(x)))

pairs = [(1, 3), (2, 1), (4, 2)]
print(sorted(pairs, key=lambda x: x[1]))

data = [10, 3, 7]
print(sorted(data, key=lambda x: -x))
