class Solution(object):
	def findRepeatedDna(self, s):
		seqs, repeated = set(), set()
		for i in xrange(len(s) - 9):
			seq = s[i:i+10]
			if seq not in seqs:
				seqs.add(seq)
			else:
				repeated.add(seq)
		return list(repeated)

if __name__ == '__main__':
	s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
	print Solution().findRepeatedDna(s)