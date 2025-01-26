def solve(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare mid element with the rightmost element
        if nums[mid] > nums[right]:
            # Minimum must be in the right half
            left = mid + 1
        else:
            # Minimum is in the left half (including mid)
            right = mid

    # After the loop, left == right points to the minimum element
    return nums[left]
