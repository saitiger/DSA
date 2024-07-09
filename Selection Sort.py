def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
    
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = 0
        is_sorted = True
        for j in range(1, n - i):
            if arr[j] > arr[max_idx]:
                max_idx = j
            if arr[j] < arr[j - 1]:
                is_sorted = False
        if max_idx != n - i - 1:
            arr[max_idx], arr[n - i - 1] = arr[n - i - 1], arr[max_idx]
        if is_sorted:
            break
    return arr

# a = [2,-3,1,4,5,0]
# selection_sort(a)
# print(a)
