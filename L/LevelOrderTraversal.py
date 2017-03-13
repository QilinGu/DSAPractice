class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrder(self, root):
		result = []
		if root is None:
			return result
		q = [root]
		while q:
			level = []
			for i in xrange(len(q)):
				node = q.pop(0)
				level.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			s = ' '.join(str(x) for x in level)
			result.append(s)
		for i, s in enumerate(result):
			print ' '* (len(result) - 1 - i) + s


if __name__ == '__main__':
	r1 = TreeNode(3)
	r1.left = TreeNode(9)
	r1.right = TreeNode(20)
	r1.right.left = TreeNode(15)
	r1.right.right = TreeNode(7)
	Solution().levelOrder(r1)