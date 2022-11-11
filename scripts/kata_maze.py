"""
Project      : Kata_Maze
Developed by : Abhay Chhagan Karade
Email        : akarade@wpi.edu

"""
import os
from utils import read_maze, get_start_end_locations, offsets

def visulization():
    pass


if __name__ == "__main__":

    maze_name = "maze2"
    filepath = os.path.join("..", "mazes", f"{maze_name}.txt")
    print("filepath",filepath)
    maze = read_maze(filepath)


    #Print maze list as it looks in .txt file
    for row in maze:
        print(row, end="\n")

    empty_spaces, start_locations, exit_locations = get_start_end_locations(maze)

    print("empty_spaces   : ",empty_spaces)
    print("start_locations: ",start_locations)
    print("exit_locations : ",exit_locations)