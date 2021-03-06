class Solution(object):
	def searchRange(self, nums, target):
		result = [-1, -1]
		if not nums:
			return result
		i, j = 0, len(nums) - 1
		while i < j:
			mid = (i+j) / 2
			if nums[mid] < target:
				i = mid + 1
			else:
				j = mid

		if nums[i] != target:
			return result
		else:
			result[0] = i
		j = len(nums) - 1

		while i < j:
			mid = (i+j+1) / 2
			if nums[mid] > target:
				j = mid - 1
			else:
				i = mid
		result[1] = j
		return result

if __name__ == '__main__':
	nums = [5, 7, 7, 8, 8, 10]
	target = 8
	print Solution().searchRange(nums, target)