def solve(nums,target):
    mpp = {}  
    for k, v in enumerate(nums):
        search_element = target - v
        if search_element in mpp:
            return [mpp[search_element], k]
        mpp[v] = k
    return []  
