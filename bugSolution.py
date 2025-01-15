import sys

def function_with_uncommon_error_solution(x, tolerance=1e-9):
    if abs(x) < tolerance:
        return 0  # Handle values close to zero
    else:
        return 1 / x

# Example demonstrating the solution
result = function_with_uncommon_error_solution(1e-100)
print(result)

result2 = function_with_uncommon_error_solution(0)
print(result2)

result3 = function_with_uncommon_error_solution(5)
print(result3)