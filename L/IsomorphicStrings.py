class Solution(object):
	def isIsomorphic(self, s, t):
		a, b, n = [-1] * 128, [-1] * 128, len(s)
		for i in xrange(n):
			if a[ord(s[i])] != b[ord(t[i])]:
				return False
			a[ord(s[i])] = i
			b[ord(t[i])] = i
		return True

if __name__ == '__main__':
	s1, t1 = 'egg', 'add'
	s2, t2 = 'foo', 'bar'
	s3, t3 = 'paper', 'title'
	print Solution().isIsomorphic(s1, t1)
	print Solution().isIsomorphic(s2, t2)
	print Solution().isIsomorphic(s3, t3)