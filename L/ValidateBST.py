class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def isValidBST(self, root):
		if root:
			node, last, stack = root, None, []
			while node or stack:
				if node:
					stack.append(node)
					node = node.left
				else:
					if last and last.val >= stack[-1].val:
						return False
					last = stack.pop()
					node = last.right
		return True

if __name__ == '__main__':
	root = TreeNode(7)
	root.left = TreeNode(2)
	root.right = TreeNode(8)
	root.left.right = TreeNode(4)
	print Solution().isValidBST(root)