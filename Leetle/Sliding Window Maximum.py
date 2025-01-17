from collections import deque

# Brute Force 
def solve(nums, k):
    if not nums or k == 0: return []
    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i:i+k]))
    return result
  
# Optimal Solution using Sliding Window 
def solve(nums, k):
  n = len(nums)
  if n == 0:
      return []
        
  deq = deque()  
  result = []
        
  for i in range(n):
      while deq and deq[0] <= i - k:
        deq.popleft()
            
      while deq and nums[i] > nums[deq[-1]]:
        deq.pop()
            
      deq.append(i)
            
      if i >= k - 1:
        result.append(nums[deq[0]])
  return result
