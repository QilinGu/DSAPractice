class Solution(object):
	def merge(self, nums1, m, nums2, n):
		result = [None]*(m+n)
		while m and n:
			if nums1[m-1] > nums2[n-1]:
				result[m+n-1] = nums1[m-1]
				m -= 1
			else:
				result[m+n-1] = nums2[n-1]
				n -= 1
		if n:
			result[:n] = nums2[:n]
		else:
			result[:m] = nums1[:m]
		return result

if __name__ == '__main__':
	nums1 = [1, 2, 5, 8]
	nums2 = [4, 7, 9]
	print Solution().merge(nums1, 4, nums2, 3)