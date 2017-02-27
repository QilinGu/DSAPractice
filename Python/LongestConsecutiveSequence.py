class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = ans = 1
        p = nums[0]
        for n in nums:
            if n - p == 0:
                continue
            elif n - p == 1:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
            p = n
        return max(ans, count)