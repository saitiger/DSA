def solve(nums):
    s = 0
    res = float('-inf')  
    for n in nums:
        s += n
        res = max(res, s)
        if s < 0:
            s = 0
    return res
