# Sum all numbers in a list
def sum_list(lst):
    return sum(lst)

lst = input("Enter numbers separated by space: ").split()
lst = [float(x) for x in lst]
print("Sum of the list:", sum_list(lst))
