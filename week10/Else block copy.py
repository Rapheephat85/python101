def divide(a, b):
    return a / b

a, b = map(int, input().split())
try:
    print(divide(a, b))
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
print("End of program")


