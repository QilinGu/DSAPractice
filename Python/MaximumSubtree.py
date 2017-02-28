class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the maximum weight node
    import sys
    def findSubtree(self, root):
        # Write your code here
        self.max_sum = -sys.maxint - 1
        self.result = None
        self.helper(root)
        return self.result
        
    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left + right + root.val > self.max_sum or self.result is None:
            self.max_sum = left + right + root.val
            self.result = root
        return left + right + root.val