# Python program to check whether the string is Symmetrical or Palindrome

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive check
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def is_symmetrical(s):
    # Symmetrical means the string is symmetric, i.e., first half == second half
    n = len(s)
    if n % 2 == 0:
        return s[:n//2] == s[n//2:]
    else:
        return s[:n//2] == s[n//2+1:]

# Test the functions
string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")

if is_symmetrical(string):
    print("The string is Symmetrical.")
else:
    print("The string is not Symmetrical.")