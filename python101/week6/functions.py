# def greet():
#     print("Hello, World!")
# greet()


# def message():
#     print('I am Arthur')
#     print('King of the Britons')
# print('I have a message for you')
# message()
# print('Goodbye')





# def main():
#     print('I have a message for you')
#     message()
#     print('Goodbye')
# def message():
#     print('I am Arthur')
#     print('King of the Britons')
# main()




# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")
# greet("Bob")
# greet("007")



# def add(a,b):
#     return a + b
# result = add(0,5)
# print(result)





# def greet(name ="World"):
#     print(f"Hello, {name}!")
# greet()
# greet("Alice")




# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2,3,4,5))



# def find_max(*args):
#     if not args:
#         return None
#     max_value = args[0]
#     for number in args:
#         if number > max_value:
#             max_value = number
#     return max_value
# result = find_max(3,5,7,2,8)
# print(f"The maximum value is: {result}")


# def print_all(*args):
#     for index, arg in enumerate(args):
#         print(f"Argument {index + 1}: {arg}")
# print_all("Python", 3.8, True, [1,2,3], {"Key": "value"})



# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# display_info(name="Alice", age=30, city="New York")


# def calculate_stats(number):
#     total_sum = sum(number)
#     # len for number
#     average = total_sum / len(number)   
#     maximun = max(number)
#     minimun = min(number)
#     return total_sum, average, maximun, minimun

# number = [5,10,15,20,25]
# total , avg , max_num , min_num = calculate_stats(number)

# print(f"Total sum: {total}")
# print(f"Average: {avg}")
# print(f"Maximum value: {max_num}")
# print(f"Minimum value: {min_num}")



def is_armstrong(number):  
    digits = str(number)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power

    return total == number
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")



