# 1. Write a Python program to read an entire text file.
def read_entire_file(filename):
    with open(filename, 'r') as f:
        return f.read()

if __name__ == "__main__":
    # Example usage: print(read_entire_file('sample.txt'))
    pass
