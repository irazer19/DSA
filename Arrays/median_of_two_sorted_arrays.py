"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Input: a[] = {-5, 3, 6, 12, 15}, b[] = {-12, -10, -6, -3, 4, 10}
Output: The median is 3.
"""


def medianOfTwoSortedArrays(arr1, arr2):
	# Time: O(log(m + n)) and Space: O(1)
	"""
	Logic:
	The objective is to find the middle in both the arrays such that the left half of both the arrays is less
	than the right half of the both arrays, and that mid is the point where we can compute the median depending on
	whether the array is length is even or odd.

	We will divide only one array to find the mid, and we will compute the mid for another array by checking
	how many more elements it should have so that the total number of elements is half.
	Once we have both the mid, we will check whether it is the point of median of the two arrays, if yes then
	we will compute the median and return, else we will move the pointer to the correct side.
	"""
	# Getting total number of elements
	total = len(arr1) + len(arr2)
	# Half number of elements
	half = total // 2
	# We will make sure that arr1 always contains <= elements than arr2. We will divide arr1.
	if len(arr1) > len(arr2):
		arr1, arr2 = arr2, arr1
	# Pointers for arr1
	l = 0
	r = len(arr1) - 1
	while True:
		# Getting the mid of array1
		mid1 = (l + r) // 2
		# Computing the mid for array2.
		# So we want in total half elements to be present in both the left half of the arrays.
		# For this 0 to mid1 elements are in array1, so the remaining elements should be in the array2
		# So our mid2 is computed accordingly.
		mid2 = half - mid1 - 2
		# The mid of both the arrays define the end of the left half of the elements (mid is inclusive).
		# So we want the border left elements to be smaller than the border right elements
		# Computing the border left and border right elements
		left1 = arr1[mid1] if mid1 >= 0 else float('-inf')
		right1 = arr1[mid1 + 1] if mid1 + 1 < len(arr1) else float('inf')
		left2 = arr2[mid2] if mid2 >= 0 else float('-inf')
		right2 = arr2[mid2 + 1] if mid2 + 1 < len(arr2) else float('inf')
		# If border left < border right, then we have found the point of median
		if left1 <= right2 and left2 <= right1:
			# If even length
			if total % 2 == 0:
				# We take the average of [max of the left border elements + min of the right border elements]
				return (max(left1, left2) + min(right1, right2)) // 2
			else:
				# If odd length, we want min of the right border elements.
				return min(right1, right2)
		# If the border left element is greater than the border right, then we will move the arr1 to the left half.
		elif left1 > right2:
			r = mid1 - 1
		else:
			# Else we will move the array1 to the right half.
			l = mid1 + 1


print(medianOfTwoSortedArrays([10, 12, 14, 16, 18, 20], [2, 3, 5, 8]))
