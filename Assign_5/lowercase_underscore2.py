# 2. Find sequences of lowercase letters joined with an underscore
import re

# Sample text
text = "hello_world this_is a_Test not_valid one_more"

# Pattern: lowercase + underscore + lowercase
pattern = r'\b[a-z]+_[a-z]+\b'

matches = re.findall(pattern, text)

print("Sequences of lowercase letters joined with underscore:")
for match in matches:
    print(match)
