class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findLCA(self, root, n1, n2):
		if root:
			if root == n1 or root == n2:
				return root
			left = self.findLCA(root.left, n1, n2)
			right = self.findLCA(root.right, n1, n2)
			if left and right:
				return root
			return left or right
		return None

if __name__ == '__main__':
	root = TreeNode(1)
	nl = TreeNode(2)
	nr = TreeNode(3)
	n1 = TreeNode(4)
	n2 = TreeNode(5)
	root.left = nl
	root.right = nr
	root.left.left = n2
	root.right.left = n1
	print Solution().findLCA(root, n1, n2).val