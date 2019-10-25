from node import Node

class Runner:
	def __init__(self, maze):
		self.open_nodes = set()
		self.visited = set()
		self.start = None
		self.end = None
		self.maze = maze
		self.completed = False
		self.mapped_maze = []

		self.find_end_points()
		self.get_open_nodes()
		
	def get_open_nodes(self):
		p = self.maze.layout
		for x in range(len(p)):
			for y in range(len(p[x])):
				if p[x][y] != self.maze.wall_char:
					self.open_nodes.add(Node((x, y)))

	def find_end_points(self):
		for x in range(len(self.maze.layout)):
			for y in range(len(self.maze.layout[x])):
				p = self.maze.layout[x][y]
				if p == self.maze.start_char:
					self.start = Node((x, y))
				elif p == self.maze.end_char:
					self.end = Node((x, y))

	def look_around(self, node):
		for i in self.open_nodes:
			if i.value[0]-1 == node.value[0] and i.value[1] == node.value[1]:
				if i not in self.visited:
					node.add_child(i)
			elif i.value[0]+1 == node.value[0] and i.value[1] == node.value[1]:
				if i not in self.visited:
					node.add_child(i)
			elif i.value[1]-1 == node.value[1] and i.value[0] == node.value[0]:
				if i not in self.visited:
					node.add_child(i)
			elif i.value[1]+1 == node.value[1] and i.value[0] == node.value[0]:
				if i not in self.visited:
					node.add_child(i)		

	def make_node_paths(self, point=None):
		if point == None:
			point = self.start
		if point not in self.visited:
			self.visited.add(point)
			if point.value == self.end.value:
				self.end = point
				self.completed = True
			else: 
				self.look_around(point)
				for i in point.children:
					path = point.path.copy()
					path.add(point.value)
					i.add_path(path)
					self.make_node_paths(i)

	def view_completed(self):
		for i in self.mapped_maze:
			print(i)

	def build_path(self, path="x"):
		other_options = set(["x", "o", "+", "*", "p"])
		maze = self.maze	
		if path == maze.start_char or path == maze.end_char or path == maze.wall_char or path == maze.open_char:
			print("Path character is already being used as a maze character trying something else...")
			for i in other_options:
				if i == maze.start_char or i == maze.end_char or i == maze.wall_char or i == maze.open_char:
					pass
				else:
					path = i
					print(f"New path character: {i}")
					break
		self.mapped_maze = [list(i) for i in maze.layout]
		for i in range(len(self.mapped_maze)):
			for j in range(len(self.mapped_maze[i])):
				if (i, j) in self.end.path and (i, j) != self.start.value:
					self.mapped_maze[i][j] = path