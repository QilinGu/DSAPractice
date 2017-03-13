class Solution(object):
	def longestPalindrome(self, s):
		self.start = 0
		self.maxL = 0
		if len(s) < 2:
			return s
		for i in xrange(len(s)-1):
			self.findPalindrome(s, i, i)
			self.findPalindrome(s, i, i+1)
		return s[self.start: self.start + self.maxL]

	def findPalindrome(self, s, m, n):
		while m >= 0 and n < len(s) and s[m] == s[n]:
			m -= 1
			n += 1
		if self.maxL < n - m - 1:
			self.start = m + 1
			self.maxL = n - m - 1

if __name__ == '__main__':
	s = 'babad'
	print Solution().longestPalindrome(s)