def nearest_smaller_element(A):
    res = [-1] * len(A)
    stack = []
    
    for i in range(len(A)):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        
        if stack:
            res[i] = A[stack[-1]]
        
        stack.append(i)
    
    return res
