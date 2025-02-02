def solve(num):
    steps = 0 
    while num:
        if num & 1: 
            num -= 1
        else: 
            num //= 2
        steps += 1  
    return steps  
