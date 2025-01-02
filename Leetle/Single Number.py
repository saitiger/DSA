def solve(nums):
  res = nums[0]
  for n in nums[1:]:
    res = res^n 
  return res 
