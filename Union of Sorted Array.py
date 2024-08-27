def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    res = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            res.append(arr2[j])
            j+= 1
        else:
            res.append(arr2[j])
            j += 1
            i += 1

    while i < m:
        res.append(arr1[i])
        i += 1

    while j < n:
        res.append(arr2[j])
        j += 1
