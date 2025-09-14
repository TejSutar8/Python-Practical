# 2. Write a Python program to multiplies all the items in a list
def multiply_list(items):
    result = 1
    for x in items:
        result *= x
    return result

if __name__ == "__main__":
    print(multiply_list([1, 2, 3, 4, 5]))  # Output: 120
