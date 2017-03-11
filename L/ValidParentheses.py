class Solution(object):
	def isValid(self, s):
		stack = []
		dic = {'(': ')', '[': ']', '{': '}'}
		for char in s:
			if char in ['(', '[', '{']:
				stack.append(char)
			else:
				if not stack:
					return False
				if char != dic[stack[-1]]:
					return False
				stack.pop()
		return not stack

if __name__ == '__main__':
	s1 = '([)]'
	s2 = '()[]{}'
	print Solution().isValid(s1)
	print Solution().isValid(s2)