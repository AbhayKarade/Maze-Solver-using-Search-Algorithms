# Kata-Maze

Kata- Maze is a maze solver for simple mazes

This coding assessment has two parts
### Part 1 : Coding 
### Part 2 : Reflection/Analysis



### Assumptions :
* Map is provided with a .txt file
* Maze is rectangular
* Start and goal pose will be selected 


## Algorithms Implemented:
1. Breadth First Search(BFS)
    - Queue data structure 
    - BFS uses First In First Out approach which makes it more suitable for searching vertices closer to the given source
    - Time complexity : O(V + E)
    - Space complexity is more critical as compared to time complexity
    - In BFS there is no concept of backtracking. 
    - BFS is optimal for finding the shortest path.
    - BFS is slow as compared to DFS.
2. Depth First Search(DFS)
    - Stack data structure.
    - DFS uses Last In First Out approach which is more suitable when there are solutions away from source.
    - Time complexity : O(V + E)
    - DFS has lesser space complexity
    - DFS is not optimal for finding the shortest path.
    - DFS algorithm is a recursive algorithm that uses the idea of backtracking



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages

```bash
pip install matplotlib
pip install numpy
```

## Running the scripts

* Aailable Mazes:
    - maze1, maze2, maze3, maze4, maze5, maze6

* Aailable Algorithms:
    - bfs     - Breadth First Search
    - dfs     - Depth First Search

To run `bfs` on `maze3`

```shell
cd Kata_Maze
python scripts/kata_maze.py --algorithm bfs --maze maze3
```

To run `dfs` on `maze6`

```shell
cd Kata_Maze
python scripts/kata_maze.py --algorithm dfs --maze maze6
```

To run the mazes which has multiple start of exit positions user have to choose the location by typing the chosen option

To run `dfs` on `maze5`

```shell
cd Kata_Maze
python scripts/kata_maze.py --algorithm dfs --maze maze5
```
Example:

```
Following Start locations are available:
0. Location: (0, 1) 
1. Location: (0, 3) 

Enter location number: 1
```



## Examples:

* White - Empty space
* Black - Obstacle boundary
* Red   - Start Pose 
* Green - Final path 
* Blue - End Pose


1. Detecting empty space 

![](/images/maze0.png)

2. Walk through a “hallway” maze

![](/images/maze2.png)

3. Find a way into and out of rooms

![](/images/maze3.png)


4. Follow winding paths 

![](/images/maze4.png)



5. Reach the end of the maze which has multiple start points

![](/images/maze5_a.png)


5. Reach the end of the maze which has multiple start points

![](/images/maze5_b.png)


7. Reach the end of the maze which has dead ends

![](/images/maze6.png)



