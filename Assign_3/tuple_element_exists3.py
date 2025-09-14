# 3. Write a Python program to check whether an element exists within a tuple
def element_in_tuple(tup, element):
    return element in tup

if __name__ == "__main__":
    print(element_in_tuple((1, 2, 3, 4), 3))  # Output: True
