def solve(num):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1 

    res = 0
    neg = num < 0  
    num = abs(num) 

    while num:
        digit = num % 10
        num //= 10  
        if res > (INT_MAX - digit) // 10:
            return 0 
        
        res = res * 10 + digit

    return -res if neg else res  
