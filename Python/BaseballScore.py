class Solution(object):
	def getScore(self, list):
		if list is None:
			return None
		stack, res = [], 0
		for c in list:
			if c not in ['Z', 'X', '+']:
				res += int(c)
				stack.append(int(c))
			elif c == 'Z':
				last = stack.pop()
				res -= last
			elif c == 'X':
				last = stack.pop()
				res += 2 * last
				stack.append(2 * last)
			else:
				l1 = stack.pop()
				l2 = stack.pop()
				score = l1 + l2
				res += score
				stack.append(l2)
				stack.append(l1)
				stack.append(score)
			print res
		return res

if __name__ == '__main__':
	lst1 = ['5', '-2', '4', 'Z', 'X', '9', '+', '+']
	r1 = Solution().getScore(lst1)
	print r1