def solve(list1, list2):
  ans = []
  i,j = 0,0 
  while i<len(list1) and j<len(list2):
    if list1[i]<=list2[j]:
      ans.append(list1[i])
      i+=1
    else:
      ans.append(list2[j])
      j+=1
  while i<len(list1):
    ans.append(list1[i])
    i+=1
  while j<len(list2):
    ans.append(list2[j])
    j+=1
  return ans 
