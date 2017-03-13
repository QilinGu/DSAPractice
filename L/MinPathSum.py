import sys
class Solution(object):
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		dp = [[sys.maxint] * n for x in range(m)]
		dp[0][0] = grid[0][0]
		for i in xrange(1, m):
			dp[i][0] = dp[i-1][0] + grid[i][0]
		for j in xrange(1, n):
			dp[0][j] = dp[0][j-1] + grid[0][j]
		for i in xrange(1, m):
			for j in xrange(1, n):
				dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		return dp[m-1][n-1]

if __name__ == '__main__':
	grid = [[2, 3, 4, 1],
	        [1, 4, 5, 7],
	        [9, 4, 2, 5]]

	print Solution().minPathSum(grid)