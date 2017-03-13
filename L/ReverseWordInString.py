class Solution(object):
	def reverseWords(self, s):
		return ' '.join(s.split()[::-1])

if __name__ == '__main__':
	s = " the sky is blue"
	print Solution().reverseWords(s)