class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSymmetric(self, root):
		if root:
			return self.check(root.left, root.right)
		return True

	def check(self, p, q):
		if not p and not q:
			return True
		if p and q and p.val == q.val:
			return self.check(p.left, q.right) and self.check(p.right, q.left)
		return False

if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(4)
	root.right.left = TreeNode(4)
	root.right.right = TreeNode(3)
	print Solution().isSymmetric(root)