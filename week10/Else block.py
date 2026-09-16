try:
    value  =int(input("Enter a number:"))   
    result = 10 / value
except ZeroDivisionError:
    print("Connot divide bt zero!")
else:
    print(f"Thr result is {result}")
print("End of program") 