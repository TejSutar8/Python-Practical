# 3. Write a Python program to create set difference
def set_difference(set1, set2):
    return set1 - set2

if __name__ == "__main__":
    print(set_difference({1, 2, 3, 4}, {2, 4}))  # Output: {1, 3}
