# 1. Demonstrate the zero division error and overflow error.
def zero_division_and_overflow():
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    try:
        import math
        b = math.exp(1000)
    except OverflowError as e:
        print("OverflowError:", e)

if __name__ == "__main__":
    zero_division_and_overflow()
