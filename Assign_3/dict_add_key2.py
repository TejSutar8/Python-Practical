# 2. Write a Python script to add a key to a dictionary
def add_key_to_dict(d, key, value):
    d[key] = value
    return d

if __name__ == "__main__":
    d = {'a': 1, 'b': 2}
    print(add_key_to_dict(d, 'c', 3))  # Output: {'a': 1, 'b': 2, 'c': 3}
