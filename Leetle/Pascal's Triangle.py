def solve(n):
  res = [[1]*(i+1) for i in range(n)]
  for i in range(n):
    for j in range(1,i):
      res[i][j] = res[i-1][j] + res[i-1][j-1]
  return res
