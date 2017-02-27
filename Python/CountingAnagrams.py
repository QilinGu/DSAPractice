class Solution(object):
	def findAnagrams(self, s, p):
		result = []
		hash = [0] * 128
		if not s or not p or len(s) == 0 or len(p) == 0:
			return result
		for c in p:
			hash[ord(c)] += 1
		l, r, count = 0, 0, len(p)
		while r < len(s):
			if hash[ord(s[r])] >= 1:
				count -= 1
			hash[ord(s[r])] -= 1
			r += 1

			if count == 0:
				result.append(l)

			if r - l == len(p):
				if hash[ord(s[l])] >= 0:
					count += 1
			hash[ord(s[l])] += 1
			l += 1
		return result

if __name__ == '__main__':
	s1, p1 = 'cbaebabacd', 'abc'
	s2, p2 = 'abab', 'ab'
	Solution().findAnagrams(s1, p1) == [0, 6]
	Solution().findAnagrams(s2, p2) == [0, 1, 2]
	print "All tests passed!"