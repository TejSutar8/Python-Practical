# Python function to sum all the numbers in a list

def sum_list(numbers):
    return sum(numbers)

# Test the function
# For simplicity, take input as space-separated numbers
input_str = input("Enter numbers separated by space: ")
numbers = [float(x) for x in input_str.split()]

total = sum_list(numbers)
print(f"The sum of {numbers} is {total}")