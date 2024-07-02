def getKthLargest(arr, k):
    sum_arr = []
    for i in range(len(arr)):
        sum = 0;
        for j in range(i, n):
            sum = sum + arr[j]
            sum_arr.append(sum)
    sum_arr.sort(reverse = True)
    return sum_arr[k - 1]

# Solution 2 using Min Heap
# from heapq import heappush, heappop
#     minHeap = []
#     for i in range(n):
#         sum = 0     
#         for j in range(i, n):
#             sum = sum + arr[j]
#             if (len(minHeap) < k):
#                 heappush(minHeap, sum)
#             else:
#                 if (minHeap[0] < sum):
#                     heappop(minHeap)
#                     heappush(minHeap, sum)
#             return minHeap[0]
