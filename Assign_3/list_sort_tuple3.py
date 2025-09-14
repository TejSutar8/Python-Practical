# 3. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
def sort_by_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])

if __name__ == "__main__":
    print(sort_by_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
    # Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
