# 3. Check if string contains only defined characters using Regex
import re

def only_defined_chars(text, allowed):
    pattern = f'^[{re.escape(allowed)}]+$'
    return bool(re.match(pattern, text))

if __name__ == "__main__":
    print(only_defined_chars('abc123', 'abc123'))  # Output: True
    print(only_defined_chars('abc123!', 'abc123'))  # Output: False
