"""
Project      : Kata_Maze
Developed by : Abhay Chhagan Karade
Email        : akarade@wpi.edu

"""

from kata_maze import read_maze, get_start_end_locations
from queue import Queue
from collections import deque
import os


def bfs(maze, start, goal):
    pass


if __name__ == "__main__":

    maze = [[0] * 3 for row in range(3)]
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result[0] == [(0, 0), (0, 1), (0, 2), (1, 2),
                         (2, 2)], "Assertion failed for Test 1"
    print("**** Test1 passed *****")

    maze = read_maze(os.path.join("..", "mazes", "maze2.txt"))
    # for row in maze:
    #     print(row)
    start_pos = (0, 4)
    goal_pos = (4, 4)
    result = bfs(maze, start_pos, goal_pos)
    assert result[0] == [(0, 4), (1, 4), (2, 4), (3, 4),
                         (4, 4)], "Assertion failed for Test 2"
    print("**** Test2 passed *****")

    maze = read_maze(os.path.join("..", "mazes", "maze2.txt"))
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result[0] is None, "Assertion failed for Test 3"
    print("**** Test3 passed *****")

    maze = read_maze(os.path.join("..", "mazes", "maze3.txt"))
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result[0] == [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)], "Assertion failed for Test 4"
    print("**** Test4 passed*****")

    print("\n**** All Test cases passed *****\n")