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
    """
    This function uses Matplotlib to show plot of maze with final path

    Following values will be assigned to variables for plotting with different colors
    empty spaces    : 0
    obstacles       : 1
    start_pos       : 2
    final path      : 3
    goal_pos        : 4

    """

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
    #To read the maze file
    filepath = os.path.join("mazes", f"{maze}.txt")
    maze = read_maze(filepath)


    # Get start and Goal location
    # If multiple locations are available ask user to choose
    _, start_pos, goal_pos = get_start_end_locations(maze)
    start = select_pose(start_pos, "Start") if (len(start_pos) > 1) else start_pos[0]
    goal = select_pose(goal_pos, "Exit") if (len(goal_pos) > 1) else goal_pos[0]
    print("\nStart : ", start)
    print("Goal  : ", goal)


    #To select the algorithm
    algos = Search(maze)
    if algorithm == "bfs":
        result,_ = algos.bfs(start, goal)

    elif algorithm == "dfs":
        result,_ = algos.dfs(start, goal)

    print("\nClose window to end this program")

    visualization(start, goal,maze, result)
    plt.show()


    print("\n**************Robot reached goal location******************")


if __name__ == "__main__":

    #To read the arguments
    Parser = argparse.ArgumentParser()
    Parser.add_argument('--algorithm', type=str, default="bfs",
                        help='Select algorithm to use on maze file')

    Parser.add_argument('--maze', type=str, choices=['maze1', 'maze2', 'maze3', 'maze4', 'maze5', 'maze6'], default='maze5',
                        help=('Choose the maze. '
                              'Can be one of: %(choices)s. Default: ' '%(default)s'))

    Args = Parser.parse_args()
    algorithm = Args.algorithm
    maze = Args.maze

    print(f"\nAlgorithm : {algorithm}, Maze: {maze}\n")

    main(algorithm, maze)
