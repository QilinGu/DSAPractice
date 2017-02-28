# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from heapq import heappop, heappush

class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        topk = []
        for p in points:
            d = ((p.x-origin.x)**2 + (p.y-origin.y)**2) ** 0.5
            heappush(topk, (-d, p))
            if len(topk) > k:
                heappop(topk)
        topk = sorted(topk, key = lambda x: (-x[0], x[1].x, x[1].y))
        return [ x[1] for x in topk]