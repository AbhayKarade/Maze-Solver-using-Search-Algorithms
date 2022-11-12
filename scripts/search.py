"""
Project      : Kata_Maze
Developed by : Abhay Chhagan Karade
Email        : akarade@wpi.edu

"""

from utils import read_maze, get_start_end_locations, is_legal_pos,get_path, offsets
from queue import Queue
from collections import deque
import os



class Search:
    def __init__(self, maze):
        self.maze = maze

    def bfs(self, start, goal):
        q = Queue()
        q.put(start)
        predecessors = {start: None}
        explored_nodes = []

        while not q.empty():
            current_pose = q.get()
            explored_nodes.append(current_pose)

            # To check if the current node is final goal node
            if current_pose == goal:
                return get_path(predecessors, start, goal), explored_nodes

            for pos in ["up", "right", "down", "left"]:
                row, col = offsets[pos]
                neighbor = ((current_pose[0] + row), (current_pose[1] + col))

                # Here we check if the neighbor is valid node and doesn't have obstacle and out of maze
                if is_legal_pos(self.maze, neighbor) and neighbor not in predecessors:
                    predecessors[neighbor] = current_pose
                    q.put(neighbor)

        return None, None


    def dfs(self, start, goal):
        stack = deque()
        stack.append(start)
        predecessors = {start: None}
        current_poses = []

        while len(stack) != 0:
            current_pos = stack.pop()
            current_poses.append(current_pos)

            # To check if the current node is final goal node
            if current_pos == goal:
                return get_path(predecessors, start, goal), current_poses

            for dir in ["up", "right", "down", "left"]:
                row, col = offsets[dir]
                neighbor = (current_pos[0]+row, current_pos[1]+col)

                # Here we check if the neighbor is valid node and doesn't have obstacle and out of maze
                if is_legal_pos(self.maze, neighbor) and neighbor not in predecessors:
                    predecessors[neighbor] = current_pos
                    stack.append(neighbor)

        return None, None



if __name__ == "__main__":

    maze = [[0] * 3 for row in range(3)]
    print("**** sample Maze ****")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    algo = Search(maze)
    result = algo.bfs(start_pos, goal_pos)
    print("Final Path: ",result[0])
    assert result[0] == [(0, 0), (0, 1), (0, 2), (1, 2),
                         (2, 2)], "Assertion failed for Test 1"
    print("**** Test1 passed ****")

    maze = read_maze(os.path.join("..", "mazes", "maze2.txt"))
    print("\n**** sample Maze2 ****")
    for row in maze:
        print(row)
    start_pos = (0, 4)
    goal_pos = (4, 4)
    algo = Search(maze)
    result = algo.bfs(start_pos, goal_pos)
    print("Final Path: ",result[0])
    assert result[0] == [(0, 4), (1, 4), (2, 4), (3, 4),
                         (4, 4)], "Assertion failed for Test 2"
    print("**** Test2 passed ****")

    maze = read_maze(os.path.join("..", "mazes", "maze2.txt"))
    print("\n**** sample Maze2 ****")
    for row in maze:
        print(row)
    start_pos = (0, 1)
    goal_pos = (3, 3)
    algo = Search(maze)
    result = algo.bfs(start_pos, goal_pos)
    print("Final Path: ",result[0])
    assert result[0] is None, "Assertion failed for Test 3"
    print("**** Test3 passed ****")

    maze = read_maze(os.path.join("..", "mazes", "maze3.txt"))
    print("\n**** sample Maze3 ****")
    for row in maze:
        print(row)
    start_pos = (0, 1)
    goal_pos = (3, 3)
    algo = Search(maze)
    result = algo.dfs(start_pos, goal_pos)
    assert result[0] == [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3)], "Assertion failed for Test 4"
    print("Final Path: ",result[0])
    print("**** Test4 passed ****")

    print("\n**** All Test cases passed *****\n")