# Program to iterate over dictionaries using for loops
my_dict = {
    'apple': 5, 
    'banana': 2, 
    'cherry': 8, 
    'mango': 1
}

print("Iterating over keys:")
for key in my_dict:
    print(key)

print("\nIterating over values:")
for value in my_dict.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in my_dict.items():
    print(key, ":", value)
