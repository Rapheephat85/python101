# def my_function():
#     local_variable = "I'm inside the function"
#     print(local_variable)
# my_function()







# global_varible = "I'm outside the function"

# def my_function():
#     print(global_varible)
# my_function()
# print(global_varible)



# import random
# HEADS = 1
# TAILE = 2
# TOSSES = 10

# def tosses_coin():
#     for toss in range(TOSSES):
#         if random.randint(HEADS, TAILE) == HEADS:
#             print('Heads')
#         else:
#             print('Tials')
# tosses_coin()



counter = 0
def increment():
    global counter
    counter += 1
increment()
increment()
increment()
print(counter)