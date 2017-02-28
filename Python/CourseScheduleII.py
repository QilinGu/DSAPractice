class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        hash = {i:[] for i in xrange(numCourses)}
        levels = [0] * numCourses
        q, ans = [], []
        for i, j in prerequisites:
            hash[j].append(i)
            levels[i] += 1
        for x in xrange(numCourses):
            if levels[x] == 0:
                q.append(x)
        
        while q:
            node = q.pop(0)
            ans.append(node)
            
            for x in hash[node]:
                levels[x] -= 1
                if levels[x] == 0:
                    q.append(x)
        
        if len(ans) == numCourses:
            return ans
        return []