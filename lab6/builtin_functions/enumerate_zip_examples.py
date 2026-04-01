a = ["A", "B", "C"]
b = [1, 2, 3]

for i, v in enumerate(a):
    print(i, v)

for x, y in zip(a, b):
    print(x, y)

x = "10"
print(type(x))
x = int(x)
print(type(x))