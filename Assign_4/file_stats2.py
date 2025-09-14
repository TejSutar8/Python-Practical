# 2. Write a Python program to compute the number of characters, words and lines in a file.
def file_stats(filename):
    with open(filename, 'r') as f:
        text = f.read()
    lines = text.splitlines()
    words = text.split()
    chars = len(text)
    return {'lines': len(lines), 'words': len(words), 'characters': chars}

if __name__ == "__main__":
    # Example usage: print(file_stats('sample.txt'))
    pass
