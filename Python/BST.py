class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def addNode(self, root, num):
		while root.left or root.right:
			if num > root.val and root.right:
				root = root.right
			elif num < root.val and root.left:
				root = root.left
			else:
				break;
		if num > root.val:
			root.right = TreeNode(num)
		else:
			root.left = TreeNode(num)

	def distanceOnBST(self, nums, n1, n2):
		if nums is None or len(nums) == 0 or not n1 or not n2:
			return -1
		root = TreeNode(nums[0])
		nums.pop(0)
		while len(nums) > 0:
			self.addNode(root, nums[0])
			nums.pop(0)
		lca = self.findLCA(root, n1, n2)
		return self.pathLength(lca, n1) + self.pathLength(lca, n2)
		# return lca.val

	def findLCA(self, root, n1, n2):
		if root is not None:
			if root.val == n1 or root.val == n2:
				return root
			left = self.findLCA(root.left, n1, n2)
			right = self.findLCA(root.right, n1, n2)
			if left and right:
				return root
			return left or right
		return None

	def pathLength(self, p, c):
		if p:
			if p.val == c:
				return 0
			leftL = self.pathLength(p.left, c)
			rightL = self.pathLength(p.right, c)
			if leftL != -1:
				return leftL + 1
			if rightL != -1:
				return rightL + 1
			else:
				return -1
		return -1

if __name__ == '__main__':
	nums1 = [5, 6, 3, 1, 2, 4]
	nums2 = [3, 2, 5, 6, 7, 1]
	d1 = Solution().distanceOnBST(nums1, 2, 4)
	d2 = Solution().distanceOnBST(nums2, 2, 7)
	# d = Solution().distanceOnBST(nums1, None, 4)
	# root2 = Solution().distanceOnBST(nums2)
	# Solution().arrayToBST(nums1).left.val == 3
	# Solution().arrayToBST(nums1).right.val == 6
	# print root.val
	# print root.right.val
	# print root.left.val
	# print root.left.left.val
	# print root.left.right.val
	# print root.left.left.right.val

	# print root2.val
	# print root2.left.val
	# print root2.right.val
	# print root2.right.right.val
	# print root2.right.right.right.val
	# print root2.left.left.val
	print d1
	print d2
	print "All tests passed!"



