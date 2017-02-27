from heapq import heappush, heappop

class Solution(object):
	def minStepMaze(self, maze, start, des):
		dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		m, n = len(maze), len(maze[0])
		q = [(0, start[0], start[1])]
		while q:
			d, r, c = heappop(q)
			if maze[r][c] == 2:
				continue
			if des[0] == r and des[1] == c:
				return d
			maze[r][c] = 2

			for di, dj in dirs:
				i, j, steps = r, c, 0
				while 0 <= i + di < m and 0 <= j + dj < n and maze[i+di][j+dj] != 1:
					i += di
					j += dj
					steps += 1
				heappush(q, (d + steps, i, j))
		return -1


if __name__ == '__main__':
	maze1 = [[0, 0, 1, 0, 0],
	        [0, 0, 0, 0, 0],
	        [0, 0, 0, 1, 0],
	        [1, 1, 0, 1, 1],
	        [0, 0, 0, 0, 0]]

	maze2 = [[0, 0, 1, 0, 0],
	        [0, 0, 0, 0, 0],
	        [0, 0, 0, 1, 0],
	        [1, 1, 0, 1, 1],
	        [0, 0, 0, 0, 0]]

	s1, d1 = [0, 4], [4, 4]
	s2, d2 = [0, 4], [3, 2]
	r1 = Solution().minStepMaze(maze1, s1, d1)
	r2 = Solution().minStepMaze(maze2, s2, d2)

	print r1
	print r2




