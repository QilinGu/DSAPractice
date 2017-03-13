class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def maxDepth(self, root):
		if not root:
			return 0
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.left = TreeNode(3)
	root.right = TreeNode(4)
	print Solution().maxDepth(root)
