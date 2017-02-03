import sys
import math
import copy
from collections import deque

class Node:
	def __init__(self, state, cost, npuzzle, updatePath):
		self.c = cost
		self.s = state
		self.n = npuzzle
		self.path = updatePath

	def getNeighbors(self, dontList):
		x = self.s.index(0);
		new = copy.copy(self.s)
		updatedPath = copy.copy(self.path)
		res = []

		#try to swap left
		if (x-1) >= 0:
			if (x%self.n != 0):
				new[x],new[x-1]=new[x-1],new[x]
				if not new in dontList:	
					res.append(Node(copy.copy(new),self.c+1,self.n,copy.copy(updatedPath + 'left'.split())))
				new = copy.copy(self.s)

		#try to swap right
		if (x+1) < len(self.s):
			if not (x+1) in [self.n*i for i in xrange(1,self.n+1)]:
				new[x],new[x+1]=new[x+1],new[x]
				if not new in dontList:
					res.append(Node(copy.copy(new),self.c+1,self.n,copy.copy(updatedPath+ 'right'.split())))
				new = copy.copy(self.s)

		#try to swap up
		if (x-self.n) >=0:
			new[x],new[x-self.n]=new[x-self.n],new[x]
			if not new in dontList:		
				res.append(Node(copy.copy(new),self.c+1,self.n,copy.copy(updatedPath + 'up'.split())))
			new = copy.copy(self.s)

		#try to swap down
		if (x+self.n) < len(self.s):
			if (x-self.n) < len(self.s):
				new[x],new[x+self.n]=new[x+self.n],new[x]
				if not new in dontList:	
					res.append(Node(copy.copy(new),self.c+1,self.n,copy.copy(updatedPath + 'down'.split())))
				new = copy.copy(self.s)

		return res

if __name__ == "__main__":
	goal = []
	search_type = sys.argv[1]
	initial_node = Node(map(int,sys.argv[2].split(',')),0,int(math.sqrt(len(sys.argv[2].split(',')))),[])
	for i in xrange(0,len(initial_node.s)):
		goal.append(i)

	if search_type == 'bfs':
		explored = []
		frontier = deque()
		frontier.append(initial_node)

		while len(frontier):
			current = frontier.popleft()
			if current.s == goal:
				print current.s
				print '{0}:{1}'.format('cost',current.c)
				print 'path {0}'.format(current.path)
				break

			explored.append(current.s)
			for neighbor in current.getNeighbors(explored):
				frontier.append(neighbor)

	if search_type == 'dfs':
		explored = []
		frontier = []
		frontier.append(initial_node)

		while len(frontier):
			current = frontier.pop()
			if current.s == goal:
				print current.s
				print '{0}:{1}'.format('cost',current.c)
				print 'path {0}'.format(current.path)
				break

			explored.append(current.s)
			for neighbor in current.getNeighbors(explored):
				frontier.append(neighbor)


