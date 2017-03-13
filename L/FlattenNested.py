class Solution(object):
	def flatten(self, arr):
		# if not isinstance(arr, (list, tuple)):
		# 	return [arr]
		# else:
		# 	result = []
		# 	for item in arr:
		# 		result += self.flatten(item)
		# return result

		# for i, x in enumerate(arr):
		# 	while i < len(arr) and isinstance(arr[i], (list, tuple)):
		# 		arr[i:i+1] = arr[i]
		# return arr

		q, result = arr, []
		while q:
			top = q[0]
			if not isinstance(top, (list, tuple)):
				result.append(q.pop(0))
			else:
				q = q[0] + q[1:]
		return result

if __name__ == '__main__':
    arr = [[[1,2],3],[4,[5,6]],[7,8,9], 2, 4, [3, 5]]
    r = Solution().flatten(arr)
    print type(r)
    for x in r:
    	print x