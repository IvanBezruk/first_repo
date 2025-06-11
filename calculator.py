#calculator.py

import sys

if len(sys.argv)!= 4:
    print("Usage: python calculator.py <number1> <operator> <number2>")
else:
    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])

        if operator == '+':
            result = num1 + num2

print(__file__)