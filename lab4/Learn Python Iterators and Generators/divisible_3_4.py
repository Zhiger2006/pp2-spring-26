def divisible(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for val in divisible(n):
    print(val, end=" ")
print()
