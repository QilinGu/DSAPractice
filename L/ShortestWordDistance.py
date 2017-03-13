class Solution(object):
	def shortestDistance(self, words, word1, word2):
		length = len(words)
		p1, p2, ans = length, length, length
		for i in xrange(len(words)):
			if words[i] == word1:
				p1 = i
				ans = min(ans, abs(p1-p2))
			elif words[i] == word2:
				p2 = i
				ans = min(ans, abs(p1-p2))
		return ans



if __name__ == '__main__':
	words = ["a","b", "c", "d"]
	word1, word2 = "a", "d"
	print Solution().shortestDistance(words, word1, word2)