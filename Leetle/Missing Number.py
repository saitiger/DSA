def solve(nums):
  s = 0
  n = len(nums)
  target_sum = (n*(n+1))/2
  for i in range(len(nums)):
    s+=nums[i]
  return target_sum-s
  # nums.sort()
  # for i in range(len(nums)):
  #     if nums[i] != i:
  #         return i
  # return len(nums)
