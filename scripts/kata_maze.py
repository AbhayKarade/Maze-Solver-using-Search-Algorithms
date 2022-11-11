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



if __name__ == "__main__":

    maze_name = "maze5"
    filepath = os.path.join("..", "mazes", f"{maze_name}.txt")
    print("filepath",filepath)
    maze = read_maze(filepath)

    #Print maze list as it looks in .txt file
    for row in maze:
        print(row, end="\n")
