class Solution(object):
	def maxSubArray(self, nums):
		# dp = [None] * len(nums)
		# dp[0] = nums[0]
		# for i in xrange(1, len(nums)):
		# 	dp[i] = nums[i] + max(0, dp[i-1])
		# return max(dp)
		maxSum, minSum, sum = nums[0], 0, 0
		start, end = 0, 0
		for i in xrange(len(nums)):
			sum += nums[i]
			if sum - minSum > maxSum:
				maxSum = sum - minSum
				end = i
			if sum < minSum:
				minSum = sum
				start = i + 1
		return nums[start:end+1]

if __name__ == '__main__':
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print Solution().maxSubArray(nums)