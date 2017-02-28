class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        # Write your code here
        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True
        if len(hash) == 0:
            return len(s)
        else:
            return len(s) - len(hash) + 1