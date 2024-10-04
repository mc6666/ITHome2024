def quick_sort(arr):
    # Base case: arrays with 1 or 0 elements are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here, the last element of the array)
    pivot = arr[len(arr) - 1]
    
    # Partition the array into two sub-arrays
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to the pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than the pivot
    
    # Recursively apply quicksort to the left and right sub-arrays
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)
