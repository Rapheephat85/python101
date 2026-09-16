class NegativeNumberError(Exception):
    def __init__(self , value):
        self.value = value
        super().__init__(f"Negative number error: {value} is not allowed.")
def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"{number} is a positive number.")
try:
    number = int(input("Enter a positive number: "))
    check_positive(number)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
finally:
    print("Execution completed.")