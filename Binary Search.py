def binary_search(arr,tar):
    n = len(arr)
    l,r = 0,n-1
    
    while(l<=r):
        # m = (l+r)//2 Possible Overflow
        m = l + (r-l)//2
        if(arr[m]==tar):
            return m
        elif(arr[m]>tar):
            r = m - 1
        else:
            l = m + 1 
    return "Not Found"

# a = [1,3,5,2,4]
# print(binary_search(a,1))
# print(binary_search(a,6))
