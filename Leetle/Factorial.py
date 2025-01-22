def solve(n):
  if n==0: 
    return 1 
  return n*solve(n-1)
