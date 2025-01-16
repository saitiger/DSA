def solve(s):
# Solution 1 
    stk = []
    ans = []
    
    for word in s.split():
        stk.append(word)
    
    while stk:
        ans.append(stk.pop())
    
    return " ".join(ans)
  
# Solution 2 
def solve(s):
    return ' '.join(reversed(s.split()))
    # Same way without using reversed
    ls = []
    for word in s.split():
        ls.append(word)
    ans = " ".join(ls[::-1])
    return ans
