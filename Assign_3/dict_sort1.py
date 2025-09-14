# 1. Write a Python script to sort (ascending and descending) a dictionary by value
def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

if __name__ == "__main__":
    d = {'a': 3, 'b': 1, 'c': 2}
    print(sort_dict_by_value(d))      # Output: {'b': 1, 'c': 2, 'a': 3}
    print(sort_dict_by_value(d, True)) # Output: {'a': 3, 'c': 2, 'b': 1}
