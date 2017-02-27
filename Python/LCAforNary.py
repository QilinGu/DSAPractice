class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.children = []
	def addChild(self, c):
		self.children.append(c)

class Solution(object):
	def findLCA(self, root, e1, e2):
		if not root:
			return None
		if root == e1 or root == e2:
			return root
		count, tmp = 0, None
		for child in root.children:
			res = self.findLCA(child, e1, e2)
			if res:
				count += 1
				tmp = res
		if count == 2:
			return root
		return tmp

	def commonManager(self, ceo, e1, e2):
		if not e1 or not e2:
			return None
		res = self.findLCA(ceo, e1, e2)
		if res == ceo:
			return None
		return res

if __name__ == '__main__':
	ceo = TreeNode('ceo')
	vp1 = TreeNode('vp1')
	vp2 = TreeNode('vp2')
	vp3 = TreeNode('vp3')
	dr1 = TreeNode('dr1')
	dr2 = TreeNode('dr2')
	dr3 = TreeNode('dr3')
	dr4 = TreeNode('dr4')
	dr5 = TreeNode('dr5')
	dr6 = TreeNode('dr6')
	ma1 = TreeNode('ma1')
	ma2 = TreeNode('ma2')
	ma3 = TreeNode('ma3')
	ma4 = TreeNode('ma4')
	ma5 = TreeNode('ma5')
	ma6 = TreeNode('ma6')
	eg1 = TreeNode('eg1')
	eg2 = TreeNode('eg2')
	eg3 = TreeNode('eg3')
	eg4 = TreeNode('eg4')
	eg5 = TreeNode('eg5')
	eg6 = TreeNode('eg6')
	ceo.addChild(vp1)
	ceo.addChild(vp2)
	ceo.addChild(vp3)
	vp1.addChild(dr1)
	vp1.addChild(dr2)
	vp1.addChild(dr3)
	vp2.addChild(dr4)
	vp3.addChild(dr5)
	vp3.addChild(dr6)
	dr1.addChild(ma1)
	dr2.addChild(ma2)
	dr2.addChild(ma3)
	dr3.addChild(ma4)
	dr5.addChild(ma5)
	dr5.addChild(ma6)
	ma2.addChild(eg1)
	ma2.addChild(eg2)
	ma4.addChild(eg3)
	ma5.addChild(eg4)
	ma5.addChild(eg5)
	ma5.addChild(eg6)

	m1 = Solution().commonManager(ceo, ma6, eg5)
	print m1.data
	# print m2.data
	print "All tests passed!"

