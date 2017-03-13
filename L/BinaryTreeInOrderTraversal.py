class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inorderTraversal(self, root):
		if not root:
			return []
		left = self.inorderTraversal(root.left)
		right = self.inorderTraversal(root.right)
		return left + [root.val] + right

if __name__ == '__main__':
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	print Solution().inorderTraversal(root)