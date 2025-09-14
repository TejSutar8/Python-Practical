# Python program to check if a string is Symmetrical or Palindrome

string = input("Enter a string: ")

# Check Palindrome
if string == string[::-1]:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")

# Check Symmetrical
mid = len(string) // 2

if len(string) % 2 == 0:   # even length
    first_half = string[:mid]
    second_half = string[mid:]
else:                      # odd length (ignore middle char for symmetry)
    first_half = string[:mid]
    second_half = string[mid+1:]

if first_half == second_half:
    print("The string is Symmetrical")
else:
    print("The string is not Symmetrical")
