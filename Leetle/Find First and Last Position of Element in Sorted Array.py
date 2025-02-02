def solve(nums, target):
    def binary_search_left():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:  
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def binary_search_right():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:  
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    start = binary_search_left()
    end = binary_search_right()
    
    if start <= end:
        return [start, end]
    return [-1, -1] 
