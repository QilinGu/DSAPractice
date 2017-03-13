class Solution(object):
	def searchMatrix(self, matrix, target):
		if not matrix:
			return False
		m, n = len(matrix), len(matrix[0])
		l, r = 0, m * n - 1
		while l <= r:
			mid = (l+r) / 2
			num = matrix[mid / n][mid % n]
			if num == target:
				return True
			elif num < target:
				l = mid + 1
			else:
				r = mid - 1
		return False


if __name__ == '__main__':
	matrix = [[1, 3, 5, 7],
	          [10, 11, 16, 20],
	          [23, 30, 34, 50]]
	target = 5
	print Solution().searchMatrix(matrix, target)