# 2. Find sequences of lowercase letters joined with an underscore
import re

def find_sequences(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

if __name__ == "__main__":
    print(find_sequences('abc_def ghi_jkl mnoP_qrs'))  # Output: ['abc_def', 'ghi_jkl']
