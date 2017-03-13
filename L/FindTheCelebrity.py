def knows(a, b):
	if a <= b:
		return True
	return False


class Solution(object):
	def findCelebrity(self, n):
		x = 0
		for i in xrange(n):
			if knows(x, i):
				x = i

		for i in xrange(n):
			if (knows(x, i) and i != x) or not knows(i, x):
				return -1

		return x

if __name__ == '__main__':
	print Solution().findCelebrity(9)