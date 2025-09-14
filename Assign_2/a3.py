# Remove i'th character from string in different ways
s = input("Enter a string: ")
i = int(input("Enter the index to remove: "))
# Method 1: Using slicing
removed1 = s[:i] + s[i+1:]
print("After removal (slicing):", removed1)
# Method 2: Using list and pop
temp = list(s)
temp.pop(i)
removed2 = ''.join(temp)
print("After removal (list pop):", removed2)
# Method 3: Using replace (removes first occurrence)
removed3 = s.replace(s[i], '', 1)
print("After removal (replace):", removed3)
