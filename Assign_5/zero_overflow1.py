# 1. Demonstrate the zero division error and overflow error.
import math

# Demonstrate ZeroDivisionError
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
except ZeroDivisionError as e:
    print("ZeroDivisionError caught:", e)

# Demonstrate OverflowError

try:
    result = math.exp(1000)  # Exponentially large number
except OverflowError as e:
    print("OverflowError caught:", e)