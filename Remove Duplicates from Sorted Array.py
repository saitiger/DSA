def solve(nums):
    if not nums:
        return 0 
    unique_idx = 0  # Points to the last unique element
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_idx]:  
            unique_idx += 1  
            nums[unique_idx] = nums[i]  
    return unique_idx + 1  

# Returning only the new length 
def solve(nums):
  new_len = 1
  if len(nums)==0: return 0
  for i in range(1,len(nums)):
    if nums[i-1]!=nums[i]:
      new_len+=1
  return new_len
