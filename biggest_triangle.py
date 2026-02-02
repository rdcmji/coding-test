import sys
sys.setrecursionlimit(200000)
def solution(grid):
	answer = 0
	area = 0
	route = set()
	path = set()
	togo = set()
	def findPath(i,j,k):
		nonlocal area
		idx = (i,j,k)
		oppsite = (i,j,-k)
		if oppsite in path:
			if oppsite not in route:
				togo.add(idx)
			return
		if oppsite not in route:
			togo.add(oppsite)
		if idx in togo:
			togo.remove(idx)
		path.add(idx)
		route.add(idx)
		area += 1
		if grid[i][j] == 1:
			direction = ['UP', 'LEFT'] if k == 1 else ['DOWN', 'RIGHT']
		else:
			direction = ['LEFT', 'DOWN'] if k == 1 else ['UP', 'RIGHT']

		for d in direction:
			if d == 'UP':
				if i > 0:
					target_k = -1 if grid[i-1][j] == 1 else 1
					if (i-1,j,target_k) not in path:
						findPath(i-1,j,target_k)
			elif d == 'LEFT':
				if j > 0:
					if (i, j-1, -1) not in path:
						findPath(i, j-1, -1)
			elif d == 'DOWN':
				if i < len(grid) -1:
					target_k = 1 if grid[i+1][j] == 1 else -1 
					if (i+1, j, target_k) not in path:
						findPath(i+1, j, target_k)
			elif d == 'RIGHT':
				if j < len(grid[0]) -1:
					if (i,j+1,1) not in path:
						findPath(i,j+1,1)

	togo.add((0,0,1))
	while(len(togo) != 0):
		path = set()
		area = 0
		findPath(*togo.pop())
		answer = max(answer, area)

	return answer

