def function_with_uncommon_error(x):
    if x == 0:
        return 0  # Correct handling of x == 0
    else:
        return 1 / x  # Potential ZeroDivisionError if x is very small

#Example showing the bug:
result = function_with_uncommon_error(1e-100)
print(result)