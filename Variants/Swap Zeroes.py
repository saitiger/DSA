# Original Leetcode 283 
# Variant : Move all the zeroes to the beginning instead of the end 

swap_idx = len(nums)-1
for i in range(len(nums)-1,-1,-1):
  if nums[i]!=0:
    nums[i],nums[swap_idx] = nums[swap_idx],nums[i]
    swap_idx-=1
return nums
