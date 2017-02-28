# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        dict = {}
        if head is None:
            return head
        dict[head] = RandomListNode(head.label)
        node = head
        while node:
            if node.next:
                if node.next not in dict:
                    dict[node.next] = RandomListNode(node.next.label)
                dict[node].next = dict[node.next]
            if node.random:
                if node.random not in dict:
                    dict[node.random] = RandomListNode(node.random.label)
                dict[node].random = dict[node.random]
            node = node.next
        return dict[head]