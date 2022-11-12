"""
Project      : Kata_Maze
Developed by : Abhay Chhagan Karade
Email        : akarade@wpi.edu

"""
import argparse
import os

from utils import read_maze, get_start_end_locations,select_pose

from search import Search

from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np


def visualization(start_pos, goal_pos, feed_maze, result):
    '''
    This function uses Matplotlib to show plot of maze with final path

    Following values will be assigned to variables for plotting 
    empty spaces    : 0
    obstacles       : 1
    start_pos       : 2
    final path      : 3
    goal_pos        : 4

    '''

    coloring = {0: "white",
                1: "black",
                2: "red",
                3: "green",
                4: "blue"}

    # Final Path
    for i in result:
        row, col = i
        feed_maze[row][col] = 3

    # Start Position
    feed_maze[start_pos[0]][start_pos[1]] = 2

    # Goal Position
    feed_maze[goal_pos[0]][goal_pos[1]] = 4

    unique_values = np.unique(feed_maze)
    colormap = colors.ListedColormap([coloring[i] for i in unique_values])
    plt.imshow(feed_maze, cmap=colormap)


def main(algorithm,maze):

    filepath = os.path.join("..", "mazes", f"{maze}.txt")

    maze = read_maze(filepath)

    # Get start and Goal location
    _, start_pos, goal_pos = get_start_end_locations(maze)

    if len(start_pos) > 1:
        start = select_pose(start_pos, "Start")
    else:
        start = start_pos[0]

    if len(goal_pos) > 1:
        goal = select_pose(goal_pos, "Exit")
    else:
        goal = goal_pos[0]

    print("\nStart : ", start)
    print("Goal  : ", goal)

    algos = Search(maze)

    if algorithm == "bfs":
        result, explored_nodes = algos.bfs(start, goal)

    elif algorithm == "dfs":
        result, explored_nodes = algos.dfs(start, goal)

    visualization(start, goal,
                  maze, result)

    plt.show()

    print("\n**************Robot reached goal location******************")


if __name__ == "__main__":

    Parser = argparse.ArgumentParser()
    Parser.add_argument('--algorithm', type=str, default="bfs",
                        help='Select algorithm to use on maze file')

    Parser.add_argument('--maze', type=str, choices=['maze1', 'maze2', 'maze3', 'maze4', 'maze5'], default='maze5',
                        help=('Choose the maze. '
                              'Can be one of: %(choices)s. Default: ' '%(default)s'))

    Args = Parser.parse_args()
    algorithm = Args.algorithm
    maze = Args.maze

    print(f"\nAlgorithm : {algorithm}, Maze: {maze}\n")

    main(algorithm, maze)
