# SPECIES: Bear and Species

# cases: 1 <= T <= 50
# grid:  2 <= N <= 50

import sys, re

def island_count(island):
	if 'G' in island and len(island) > 1:
		return 0
	if 'P' in island and 'B' in island:
		return 0
	if '?' in island and 'P' not in island and 'B' not in island:
		if len(island) == 1:
			return 3
		return 2
	return 1

class BearGrid:
	def __init__(self, grid):
		self.grid = grid
		self.n = len(grid)
		self.visited = [[False for r in range(self.n)] for c in range(self.n)]
		self.stack = []
		self.islands = []
		self.depth = 0
		self.current_island = ''

	# check the specified cell
	def check_cell(self, r, c):
		# base case: out of bounds, return '.'
		if r < 0 or r > n-1 or c < 0 or c > n-1:
			return '.'
		# base case: already visited, return existing value
		if self.visited[r][c]:
			return self.grid[r][c]
		# mark as visited
		self.visited[r][c] = True
		# check cell
		cell = self.grid[r][c]
		if '.' != cell:
			self.current_island = self.current_island + cell
			self.stack.append([r-1,c])
			self.stack.append([r+1,c])
			self.stack.append([r,c-1])
			self.stack.append([r,c+1])
		return cell

	def validate(self):
		for r in range(self.n):
			for c in range(self.n):
				self.check_cell(r,c)
				while self.stack:
					next = self.stack.pop()
					self.check_cell(next[0],next[1])
				self.islands.append(self.current_island)
				self.current_island = ''
		options = 1
		for island in self.islands:
			options = options * island_count(island)
		return options


a = sys.stdin.buffer.read().split()

# number of test cases
cases = int(a[0])
i = 1

for case in range(cases):

	# grid size for this test case
	n = int(a[i])
	i = i+1

	# build a grid for each test case
	grid = [None]*n
	for r in range(n):
		row = a[i]
		i = i+1
		g = [None]*n
		for c in range(n):
			g[c] = chr(row[c])
		grid[r] = g

	bg = BearGrid(grid)
	options = bg.validate()

#	print('grid',bg.grid)
#	print('islands',bg.islands)
	print(options % (10**9 + 7))
