class Solution(object):
	def permute(self, nums):
		self.result = []
		self.dfs(nums, [])
		return self.result

	def dfs(self, A, tmp):
		if not A:
			self.result.append(tmp)
			return
		for i, num in enumerate(A):
			self.dfs(A[:i] + A[i+1:], tmp + [num])


if __name__ == '__main__':
	nums = [1, 2, 3]
	print Solution().permute(nums)
