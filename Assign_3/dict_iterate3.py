# 3. Write a Python program to iterate over dictionaries using for loops
def iterate_dict(d):
    return [(k, v) for k, v in d.items()]

if __name__ == "__main__":
    d = {'a': 1, 'b': 2, 'c': 3}
    print(iterate_dict(d))  # Output: [('a', 1), ('b', 2), ('c', 3)]
