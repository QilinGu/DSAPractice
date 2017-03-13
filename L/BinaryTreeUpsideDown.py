class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def upsideDownBT(self, root):
		if not root or not root.left:
			return root
		newRoot = self.upsideDownBT(root.left)
		root.left.left = root.right
		root.left.right = root
		root.left = None
		root.right = None
		return newRoot