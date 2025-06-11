#adder.py
import sys

if len(sys.argv) != 3:
    print("Usage: python adder.py <number1> <number2>")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        sum = num1 + num2
        print("The sum is:", sum)
    except ValueError:
        print("Error: Please provide valid numbers.")