# Function to calculate the total sum of elements in a list
def total_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

# Example usage
numbers = [5, 10, 15, 20]

result = total_sum(numbers)

print("The list is:", numbers)
print("The total sum is:", result)
