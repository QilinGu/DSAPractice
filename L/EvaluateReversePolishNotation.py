class Solution(object):
	def evalRPN(self, tokens):
		stack = []
		for t in tokens:
			if t not in ['+', '-', '*', '/']:
				stack.append(int(t))
			else:
				n2, n1 = stack.pop(), stack.pop()
				if t == '+':
					stack.append(n1 + n2)
				elif t == '-':
					stack.append(n1 - n2)
				elif t == '*':
					stack.append(n1 * n2)
				else:
					if n1*n2 < 0 and n1 % n2 != 0:
						stack.append(n1 / n2 + 1)
					else:
						stack.append(n1 / n2)
		return stack.pop()

if __name__ == '__main__':
	tokens = ["2", "1", "+", "3", "*"]
	print Solution().evalRPN(tokens)