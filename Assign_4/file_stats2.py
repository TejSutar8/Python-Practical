# Program to compute the number of characters, words, and lines in a file

filename = "Assign_4/sample2.txt"

# Open the file
with open(filename, "r") as file:
    lines = file.readlines()

# Count lines
num_lines = len(lines)

# Count words and characters
num_words = 0
num_chars = 0

for line in lines:
    words = line.split()
    num_words += len(words)
    num_chars += len(line)

print("Number of lines:", num_lines)
print("Number of words:", num_words)
print("Number of characters:", num_chars)
