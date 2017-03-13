class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findLeaves(self, root):
		self.result = []
		self.dfs(root)
		return self.result

	def dfs(self, node):
		if not node:
			return 0
		level = max(self.dfs(node.left), self.dfs(node.right)) + 1
		if len(self.result) < level:
			self.result.append([])
		self.result[level-1].append(node.val)
		node.val = None
		return level


if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	print Solution().findLeaves(root)