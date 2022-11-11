"""
Project      : Kata_Maze
Developed by : Abhay Chhagan Karade
Email        : akarade@wpi.edu

"""
import os

def read_maze(file_name):
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