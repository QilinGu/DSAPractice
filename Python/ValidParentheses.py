class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		rtype: bool
		"""
		stack = []
		dict = {'(': ')', '{': '}', '[': ']'}
		for char in s:
			if char in ['(', '{', '[']:
				stack.append(char)
			else:
				if not stack:
					return False
				if char != dict[stack[-1]]:
					return False
				stack.pop()
		return not stack


if __name__ == '__main__':
	s1 = ''
	s2 = '('
	s3 = '()'
	s4 = '()[]{}'
	s5 = '([)]'
	s6 = '[6748(adka)dka]'
	Solution().isValid(s1) == True
	Solution().isValid(s2) == False
	Solution().isValid(s3) == True
	Solution().isValid(s4) == True
	Solution().isValid(s5) == False
	Solution().isValid(s6) == False
	print 'All tests passed!'
