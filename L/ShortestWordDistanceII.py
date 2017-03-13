class WordDistance(object):
	def __init__(self, words):
		self.dic = {}
		for i, w in enumerate(words):
			self.dic[w] = self.dic.get(w, []) + [i]

	def shortest(self, word1, word2):
		pa, pb = self.dic[word1], self.dic[word2]
		# i, j, ans = 0, 0, self.length
		# while i < len(a) and j < len(b):
		# 	ans = min(ans, abs(a[i]-b[j]))
		# 	if a[i] > b[j]:
		# 		j += 1
		# 	else:
		# 		i += 1
		# return ans
		return min([abs(a - b) for a in pa for b in pb ])



if __name__ == '__main__':
	words = ["a","b", "c", "d", "e", "f", "g"]
	print WordDistance(words).shortest("a", "e")
	print WordDistance(words).shortest("b", "c")