from maze import Maze
from runner import Runner

m1 = [	['#','#','#','#','#','#','#','#','#'], 
		['#','s','#',' ',' ',' ','#','e','#'], 
     	['#',' ','#',' ','#',' ',' ',' ','#'], 
     	['#',' ',' ',' ','#',' ','#',' ','#'], 
     	['#','#','#','#','#','#','#','#','#']] 

maze = Maze(layout=m1)

#maze.build_new(15, 20)
runner = Runner(maze)
runner.get_nodes()
print(runner.nodes)