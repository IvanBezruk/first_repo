'''
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
'''

"""
num = int(input("Enter your number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
"""

"""
pets =  ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        print("There are dog and cat")
    case ["dog", _, _]:
        print("There is a dog")
    case _:
        print("No dogs")
"""

"""
def string_to_code(string: str) -> dict:
    codes = {}
    for ch in string:
        if ch not in codes:
            codes[ch] = ord(ch)
    return codes

result = string_to_code("Artem")
print(result)
"""

"""
def say(message, times=1):
    print(message * times)
say('Yo')
say('No', 5)
"""

"""
def real_cost(base: int, discount: float = 0) -> float:
    return base * (1-discount)

price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f'New price of bread:{current_price_bread}')
print(f'New price of butter: {current_price_butter}')
print(f'New price of sugar: {current_price_sugar}')
"""

"""
def print_all_args(*args):
    for arg in args:
        print(arg)
print_all_args(1, 'Hello', True)
"""

"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
"""

"""
def fibonacci(n):
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print (fibonacci(10))
"""

def factorial(n):
    print("Call the function factorial with n =", n)
    if n==1:
        print("Basic approach, n =1, returning 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Returning result for n=", n, ":", result)
        return result
    
print(factorial(5))

