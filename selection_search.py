def search_small(arr):
	
	small = arr[0]
	small_index = 0

	for i in range(len(arr)):

		if arr[i] < small:

			small = arr[i]
			small_index = i

	return small_index


def selection_search(arr):

	for i in range(len(arr)):

		small_index = search_small(arr)

		changed_val = arr[i]
		arr[i] = arr[small_index]
		arr[small_index] = changed_val

	return arr

	