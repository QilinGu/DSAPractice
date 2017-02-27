from heapq import heappop, heappush
class Movie(object):
	def __init__(self, id, rating):
		self.id = id
		self.rating = rating
		self.similarMovies = []

	def getRating(self):
		return self.rating

	def getId(self):
		return self.id

	def getSimilarMovies(self):
		return self.similarMovies

	def setSimilarMovies(self, movies):
		self.similarMovies = movies

class Solution(object):
	def getMovieRecommendations(self, movie, N):
		if movie.getId is None or N is None:
			return set([])
		q, tops, visited, res = [movie], [], set([movie.getId()]), []
		while q:
			cur = q.pop(0)
			for n in cur.getSimilarMovies():
				nid, nrating = n.getId(), n.getRating()
				if nid not in visited:
					visited.add(nid)
					heappush(tops, (nrating, nid))
					if len(tops) > N:
						heappop(tops)
					q.append(n)
		while tops:
			res.append(heappop(tops)[1])
		return res


if __name__ == '__main__':
	m1 = Movie(1, 4)
	m2 = Movie(2, 7)
	m3 = Movie(3, 3)
	m4 = Movie(4, 5)
	m5 = Movie(5, 8)
	m6 = Movie(6, 5)
	m7 = Movie(7, 2)
	m8 = Movie(8, 1)
	m9 = Movie(9, 9)
	m10 = Movie(10, 6)

	# m1.setSimilarMovies([m2, m3, m5, m7, m8, m10])
	# m2.setSimilarMovies([m1, m4, m6, m7, m9])
	# m3.setSimilarMovies([m1, m4, m8])
	# m4.setSimilarMovies([m2, m3])
	# m5.setSimilarMovies([m1, m6, m10])
	# m6.setSimilarMovies([m2, m5, m8, m10])
	# m7.setSimilarMovies([m1, m2, m9])
	# m8.setSimilarMovies([m1, m3, m6, m10])
	# m9.setSimilarMovies([m2, m7, m10])
	# m10.setSimilarMovies([m1, m5, m6, m8, m9])

	m1.setSimilarMovies([m5, m7])
	m2.setSimilarMovies([m4])
	m3.setSimilarMovies([m8])
	m4.setSimilarMovies([m2, m7])
	m5.setSimilarMovies([m1, m10])
	# m6.setSimilarMovies([m2, m5, m8, m10])
	m7.setSimilarMovies([m1, m4])
	m8.setSimilarMovies([m3])
	# m9.setSimilarMovies([m8])
	m10.setSimilarMovies([m5])

	rec1 = Solution().getMovieRecommendations(m1, 4)
	rec2 = Solution().getMovieRecommendations(m2, 3)

	print rec1
	print rec2








