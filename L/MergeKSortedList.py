from heapq import heappop, heappush, heapreplace

class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		dummy = ListNode(0)
		node, q = dummy, []
		for l in lists:
			heappush(q, (l.val, l))
		while q:
			v, n = q[0]
			if not n.next:
				heappop(q)
			else:
				heapreplace(q, (n.next.val, n.next))
			node.next = n
			node = node.next
		return dummy.next

if __name__ == '__main__':
	l1 = ListNode(2)
	l2 = ListNode(5)
	l3 = ListNode(7)
	l4 = ListNode(4)
	l1.next = ListNode(3)
	l1.next.next = ListNode(10)
	l2.next = ListNode(9)
	l3.next = ListNode(8)
	l4.next = ListNode(6)
	h1 = Solution().mergeKLists([l1, l2, l3, l4])
	node = h1
	while node:
		print node.val
		node = node.next
