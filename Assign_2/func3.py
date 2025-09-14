# Python program to reverse a string

def reverse_string(s):
    return s[::-1]

# Test the function
string = input("Enter a string: ")
reversed_str = reverse_string(string)
print(f"The reversed string is: {reversed_str}")