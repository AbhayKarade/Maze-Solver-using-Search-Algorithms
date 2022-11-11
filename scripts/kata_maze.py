"""
Project      : Kata_Maze
Developed by : Abhay Chhagan Karade
Email        : akarade@wpi.edu

"""
import os
from utils import read_maze, get_start_end_locations

from search import Search

from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

def visualization(start_pos, goal_pos, feed_maze, result, explored_nodes):
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


def main(maze):
  
    filepath = os.path.join("..", "mazes", f"{maze}.txt")

    maze = read_maze(filepath)

    # Get start and Goal location
    _, start_pos, goal_pos = get_start_end_locations(maze)

    algos = Search(maze)

    result, explored_nodes = algos.bfs(start_pos[0], goal_pos[0])

    visualization(start_pos[0], goal_pos[0],
                        maze, result, explored_nodes)

    plt.show()

    print("\n**************Robot reached goal location******************")



if __name__ == "__main__":

    maze_name = "maze2"

    main(maze_name)