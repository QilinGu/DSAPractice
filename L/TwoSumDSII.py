class TwoSum(object):
	def __init__(self):
		self.num = set()
		self.sum = set()


	def add(self, number):
		if number in self.num:
			self.sum.add(number * 2)
		else:
			for n in self.num:
				self.sum.add(n + number)
			self.num.add(number)

	def find(self, value):
		return value in self.sum


if __name__ == '__main__':
	obj = TwoSum()
	obj.add(1)
	obj.add(3)
	obj.add(5)
	print obj.find(4)
	print obj.find(7)