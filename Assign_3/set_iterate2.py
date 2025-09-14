# 2. Write a Python program to iterate over sets
def iterate_set(s):
    return [item for item in s]

if __name__ == "__main__":
    print(iterate_set({1, 2, 3}))  # Output: [1, 2, 3] (order may vary)
