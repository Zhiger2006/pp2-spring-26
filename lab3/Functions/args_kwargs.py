def sum_all(*args):
    print(sum(args))

sum_all(1, 2, 3)

def show_info(**kwargs):
    print(kwargs)

show_info(name="Ali", age=19)

def multiply_all(*args):
    result = 1
    for i in args:
        result *= i
    print(result)

multiply_all(2, 3, 4)

def print_values(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

print_values(a=1, b=2)
