# Python program to reverse words in a given string

def reverse_words(s):
    # Split the string into words
    words = s.split()
    # Reverse the list of words
    words.reverse()
    # Join the words back into a string
    return ' '.join(words)

# Test the function
string = input("Enter a string: ")
reversed_string = reverse_words(string)
print(f"Reversed words: {reversed_string}")