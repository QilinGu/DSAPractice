class Solution(object):
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'C': 50, 'D': 100, 'L': 500, 'M': 1000}
        res = d[s[-1]]
        for i in xrange(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        return res

if __name__ == '__main__':
	s1 = 'XXVI'
	print Solution().romanToInt(s1)