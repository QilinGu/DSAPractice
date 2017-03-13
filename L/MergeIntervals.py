class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def merge(self, intervals):
		ans = []
		for i in sorted(intervals, key=lambda x: x.start):
			if ans and i.start <= ans[-1].end:
				ans[-1].end = max(ans[-1].end, i.end)
			else:
				ans.append(i)
		return ans

if __name__ == '__main__':
	intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
	for i in Solution().merge(intervals):
		print (i.start, i.end)