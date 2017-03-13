class Solution(object):
	def maxProduct(self, nums):
		max1, min1, ans = nums[0], nums[0], nums[0]
		for i in xrange(1, len(nums)):
			if nums[i] < 0:
				max1, min1 = min1, max1
			max1 = max(nums[i], nums[i]*max1)
			min1 = min(nums[i], nums[i]*min1)
			ans = max(ans, max1)
		return ans

if __name__ == '__main__':
	nums = [2,3,-2,4]
	print Solution().maxProduct(nums)