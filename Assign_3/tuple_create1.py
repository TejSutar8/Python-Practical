# 1. Write a Python program to create a tuple
def create_tuple(*args):
    return tuple(args)

if __name__ == "__main__":
    print(create_tuple(1, 2, 3))  # Output: (1, 2, 3)
