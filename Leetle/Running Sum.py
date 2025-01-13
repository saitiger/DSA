def solve(nums):
  ans = []
  running_sum = 0 
  for n in nums:
    running_sum+=n
    ans.append(running_sum)
  return ans

# In-place 
def solve(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

# Using In-built methods 
from itertools import accumulate
def solve(nums):
    return list(accumulate(nums))              
