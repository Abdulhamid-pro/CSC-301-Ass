# LINEAR SEARCH ASSIGNMENT
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # index where target is found
    return -1  # if not found

arr = [2, 5, 7, 10, 14, 20]
target = 10

index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found")

		
# For Linear Search	
	
# Time Complexity:
# Best Case: O(1) = target is at the first element
# Average Case: O(n) = target is at the middle
# Worst Case: O(n) = target is at the last element or not present

# Space Complexity = O(1)
