class Solution(object):
	def search(self, nums, target):
		l, r = 0, len(nums) - 1
		while l < r:
			mid = (l+r) / 2
			if nums[mid] < nums[r]:
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

if __name__ == '__main__':
	nums = [6, 7, 8, 9 , 1, 2, 3, 4, 5]
	target = 7
	print Solution().search(nums, target)

