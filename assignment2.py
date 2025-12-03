# FIBONACCI SERIES ASSIGNMENT
def fib(n):
    # direct recursion: the function calls itself
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# print first 8 Fibonacci numbers
for i in range(8):
    print(fib(i), end=" ")
    
# Output: 0 1 1 2 3 5 8 13