class Solution(object):
	def search(self, nums, target):
		l, r = 0, len(nums) - 1
		while l < r:
			mid = (l+r) / 2
			if nums[mid] < nums[-1]:
				r = mid
			else:
				l = mid + 1
		n0 = l
		l, r = 0, len(nums) - 1
		while l <= r:
			mid = (l+r) / 2
			rmid = (mid + n0) % len(nums)
			if nums[rmid] == target:
				return rmid
			elif nums[rmid] < target:
				l = mid + 1
			else:
				r = mid - 1
		return -1


