# Python program to remove i'th character from string in different ways

def remove_ith_char_slicing(s, i):
    # Using string slicing
    return s[:i] + s[i+1:]

def remove_ith_char_list(s, i):
    # Using list
    lst = list(s)
    del lst[i]
    return ''.join(lst)

def remove_ith_char_replace(s, i):
    # Using replace, but this removes all occurrences, not just i'th
    # For exact i'th, better not use this
    # But to show different way, perhaps use it if unique
    # Actually, replace is not suitable for position
    # Perhaps use string concatenation
    return s[:i] + s[i+1:]

# Test the functions
string = input("Enter a string: ")
i = int(input("Enter the position (0-based index) to remove: "))

if 0 <= i < len(string):
    print(f"Using slicing: {remove_ith_char_slicing(string, i)}")
    print(f"Using list: {remove_ith_char_list(string, i)}")
    print(f"Using concatenation: {remove_ith_char_replace(string, i)}")
else:
    print("Invalid position.")