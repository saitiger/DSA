def solve(num):
    num_copy = num
    num_digits = 0
    
    # Calculate the number of digits in num
    while num_copy:
        num_digits += 1
        num_copy //= 10
    
    num_sum = 0
    num_copy = num
    
    while num_copy:
        digit = num_copy % 10
        num_sum += digit ** num_digits
        num_copy //= 10
    
    return num_sum == num
