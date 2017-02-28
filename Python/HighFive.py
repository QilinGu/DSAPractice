'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
from heapq import heappop, heappush

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        hash, res = {}, {}
        for result in results:
            if result.id not in hash:
                hash[result.id] = []
            heappush(hash[result.id], result.score)
            if len(hash[result.id]) > 5:
                heappop(hash[result.id])
        for k, v in hash.items():
            res[k] = float(sum(v))/5
        return res