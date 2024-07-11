def Cyclic_Sort(nums):
    i = 0
    while i<len(nums):
        correct_idx = nums[i]-1
        if(nums[i]!=nums[correct_idx]):
            nums[i],nums[correct_idx] = nums[correct_idx],nums[i]
        else:
            i+=1
    return nums

# a = [3,5,2,1,4]
# print(Cyclic_Sort(a))
