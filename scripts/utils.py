"""
Project      : Kata_Maze
Developed by : Abhay Chhagan Karade
Email        : akarade@wpi.edu
"""

import os

"""
To explore neighbor nodes of current node
"""

offsets = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}


def read_maze(file_name):
    """
    To read maze from .txt file and check if it is rectangular
    """
    try:
        with open(file_name) as fn:
            maze = [[int(char) for char in line.strip("\n")] for line in fn]
            for row in maze:
                if len(row) != len(maze[0]):
                    print("The Maze is not rectangular")
                    raise SystemExit

            return maze

    except OSError:
        print("Selected folder is not accessible")
        raise SystemExit


def get_start_end_locations(maze):
    """
    To get the start and end locations in a given maze

    """
    row = 0
    empty_spaces = []
    start_locations = []
    exit_locations = []

    for lst in maze:
        empty = [(row, col) for col, val in enumerate(lst) if val == 0]
        if empty:
            empty_spaces.append(empty)

        if row == 0:
            start_locations.extend(empty)

        if row == (len(maze)-1):
            exit_locations.extend(empty)

        row = row + 1

    return empty_spaces, start_locations, exit_locations


def is_legal_pos(maze, pose):
    """
    To check if the explored pose is traversable for robot

    """
    row_size = len(maze)
    col_size = len(maze[0])
    row, col = pose
    return 0 <= row < row_size and 0 <= col < col_size and maze[row][col] != 1


def get_path(predecessors, start, goal):
    """
    To make a list of final path coordinates from the predecessor dictionary

    """
    current_pos = goal
    path = []

    while current_pos != start:
        path.append(current_pos)
        current_pos = predecessors[current_pos]

    path.append(start)
    path.reverse()
    return path


def select_pose(pose_list, location):
    """

    To select the pose from given options

    Input: 
    pose_list: list 
    location : string

    """

    print(f"Following {location} locations are available:")
    for inx, pos in enumerate(pose_list):
        print(f"{inx}. Location: {pos} ")
    while True:
        try:
            val = int(input("\nEnter location number: "))
        except:
            raise ValueError("Please choose correct value from options")
        if val < len(pose_list) and val >= 0:
            pose = pose_list[val]
            break
        print("Invalid Number")
    return pose
