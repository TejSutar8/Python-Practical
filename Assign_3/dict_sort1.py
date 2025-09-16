# Program to sort a dictionary by value

# Sample dictionary
my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'mango': 1}

print("Original dictionary:", my_dict)

# Sort by value (ascending)
asc_sort = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by value (ascending):", asc_sort)

# Sort by value (descending)
desc_sort = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Dictionary sorted by value (descending):", desc_sort)
