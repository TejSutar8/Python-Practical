# Python function to find the Max of three numbers

def max_of_three(a, b, c):
    return max(a, b, c)

# Test the function
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

maximum = max_of_three(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, {num3} is {maximum}")