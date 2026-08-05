# def factorial(n):
#     if n == 0:
#         return 1 
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))


# def fibonacci(n):
#     if n == 0:
#         return 0 
#     elif n == 1 :
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))



# def factorial_iter(n):
#     result = 1
#     for i in range(2, n + 1):
#         result += i
#     return result







def generate_primes(n):
    if n < 2:
        return []
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes





