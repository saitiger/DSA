# Leetcode 88
# Variant : We don't know the exact size of list a, the only thing we know is that it is double in size of list b and second half of list a has the space to keep the merged 
# elements 
def merge(list_a, list_b):
    a = len(list_a) // 2 - 1
    b = len(list_b) - 1
    i = len(list_a) - 1
    
    while b >= 0:
        if a >= 0 and list_a[a] >= list_b[b]:
            list_a[i] = list_a[a]
            a -= 1
        else:
            list_a[i] = list_b[b]
            b -= 1
        i -= 1
