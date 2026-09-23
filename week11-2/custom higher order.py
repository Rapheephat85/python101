def applt_twice(func, value):
    return func(func(value))
def increment(x):
    return x + 1
print(applt_twice(increment, 5))