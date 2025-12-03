# RECURSION ASSIGNMENT
def sum_numbers(n):
    # base case
    if n == 1:
        return 1
    else:
        # recursive case
        return n + sum_numbers(n - 1)

# sum of first 10 numbers
result = sum_numbers(10)
print("The sum of the first 10 numbers is:", result)

# Output: The sum of the first 10 numbers is: 55