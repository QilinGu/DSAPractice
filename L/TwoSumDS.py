class TwoSum(object):
	def __init__(self):
		self.dic = {}

	def add(self, number):
		self.dic[number] = self.dic.get(number, 0) + 1

	def find(self, value):
		for key in self.dic:
			target = value - key
			if target in self.dic and (key != target or self.dic[key] > 1):
				return True
		return False

if __name__ == '__main__':
	obj = TwoSum()
	obj.add(1)
	obj.add(3)
	obj.add(5)
	print obj.find(4)
	print obj.find(7)