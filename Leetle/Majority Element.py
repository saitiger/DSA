def solve(nums):
    cnt = 0
    el = nums[0]
    target = len(nums) // 2

    for n in nums:
        if cnt == 0:
            el = n
        cnt += 1 if n == el else -1
      
    if nums.count(el) > target:
        return el
    return False
