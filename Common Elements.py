def find_common_elements(list1, list2):
    count1 = {}
    count2 = {}
    for item in list1:
        count1[item] = count1.get(item, 0) + 1
    for item in list2:
        count2[item] = count2.get(item, 0) + 1
    common_elements = []
    for key in count1:
        if key in count2:
            common_count = min(count1[key], count2[key])
            common_elements.extend([key] * common_count)
    return common_elements

# Solution 2 
