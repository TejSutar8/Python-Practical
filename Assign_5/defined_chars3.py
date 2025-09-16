# 3. Check if string contains only defined characters using Regex

import re

# User input
text = input("Enter a string: ")

# Define allowed characters (a-z, A-Z, 0-9, and _)
pattern = r'^[a-zA-Z0-9_]+$'

if re.fullmatch(pattern, text):
    print("✅ String contains only defined characters")
else:
    print("❌ String contains characters outside the allowed set")
