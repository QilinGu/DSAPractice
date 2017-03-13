class Solution(object):
	def reverseWords(self, s):
		s.reverse()
		index = 0
		for i in xrange(len(s)):
			if s[i] == ' ':
				s[index:i] = reversed(s[index:i])
				index = i + 1
		s[index:] = reversed(s[index:])

if __name__ == '__main__':
	s = ['h','e','l','l','o',' ','w','o','r','l','d']
	print Solution().reverseWords(s)