class Solution(object):
	def permute(self, nums):
		self.result = []
		used = [0] * len(nums)
		self.dfs(sorted(nums), [], used)
		return self.result

	def dfs(self, nums, tmp, used):
		if len(nums) == len(tmp):
			self.result.append(tmp)
			return
		for i in xrange(len(nums)):
			if used[i]:
				continue
			if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
				continue
			used[i] = 1
			self.dfs(nums, tmp + [nums[i]], used)
			used[i] = 0

if __name__ == '__main__':
	nums = [1, 1, 2]
	print Solution().permute(nums)
