def solve(n):
    # Using Modulo 
    if n==0: return False
    elif n==1 or n%2==0:
      return True 
    else:
      return False
    # Using Bit manipulation
    return n>0 and (n & (n-1))==0
