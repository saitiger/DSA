def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bubble_sort(arr):
    if is_sorted(arr): # Checking if the array is sorted, if yes then return the array and not do comparisons
        return arr
    
    for i in range(len(arr)):
        swapped = False # Keeping track if elements are swapped to reduce the number of comparisons when elements are sorted in the previous run
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]: # Swapping elements if not in correct order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# a = [2,-3,1,4,5,0]
# bubble_sort(a)
# print(a)
