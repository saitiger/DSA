def count_sort(arr):
	
  K = max(arr)

	count_array = [0] * (K+1)

	for num in arr:
		count_array[num] += 1

	for i in range(1, K + 1):
		count_array[i] += count_array[i - 1]

	sorted_arr = [0] * len(arr)

	for i in range(len(input_array) - 1, -1, -1):
		sorted_arr[count_array[arr[i]] - 1] = arr[i]
		sorted_arr[input_array[i]] -= 1
	return sorted_arr
