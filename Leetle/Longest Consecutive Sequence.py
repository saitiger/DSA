def solve(nums):
  if len(nums)==0:
    return 0
  lookup = set(nums)
  cnt = 1
  max_cnt = 1
  for n in nums:
    if (n-1) in lookup:
      continue
    else:
      while n+1 in lookup:
        cnt+=1
        n = n+1
      max_cnt = max(max_cnt,cnt)
  return max_cnt
