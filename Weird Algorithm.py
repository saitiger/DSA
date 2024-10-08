while N != 1:
  print(N, end=" ")  
  if N % 2 != 0:
    N = N * 3 + 1
  else:
    N //= 2
