class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Intervals(object):
	def __init__(self):
		self.list = []

	def addInterval(self, s, e):
		if not self.list:
			self.list.append(Interval(s, e))
		else:
			i = 0
			while i < len(self.list) and self.list[i].end < s:
				i +=1
			l = i
			start, end = s, e
			while i < len(self.list) and self.list[i].start <= e:
				start = min(s, self.list[i].start)
				end = max(e, self.list[i].end)
				i += 1
			r = i
			self.list[l:r] = [Interval(start, end)]

	def getTotalCoverage(self):
		length = 0
		for i in self.list:
			length += i.end - i.start
		return length

if __name__ == '__main__':
	I = Intervals()
	I.addInterval(1, 3)
	I.addInterval(2, 4)
	I.addInterval(3, 7)
	I.addInterval(9, 12)
	I.addInterval(8, 10)
	I.addInterval(15, 18)
	I.addInterval(13, 14)
	for i in I.list:
		print (i.start, i.end)
	print I.getTotalCoverage()
