# Program to read an entire text file

# Open the file in read mode
file = open("Assign_4/sample1.txt", "r")

# Read the entire file
content = file.read()

print("Contents of the file:\n")
print(content)

# Close the file
file.close()
