class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        if k <= 0 or len(nums) < k:
            return []
        res = [0] * (len(nums) - k + 1)
        for i in xrange(k):
            res[0] += nums[i]
        for i in xrange(1, len(nums) - k + 1):
            res[i] = res[i-1] + nums[i + k - 1] - nums[i-1]
        return res