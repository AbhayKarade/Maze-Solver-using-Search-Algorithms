# [Path Robotics](https://www.path-robotics.com/) - coding assessment

# Kata-Maze


Kata- Maze is a maze solver for simple mazes.

This coding assessment has two parts
### Part 1 : Coding 
### Part 2 : Reflection/Analysis

### Assumptions :
* Map is provided with a `.txt` file.
* Maze is rectangular.
* Start and goal pose will be selected by user.


## Algorithms Implemented:
1. Breadth First Search(BFS)
    - Queue data structure. 
    - BFS uses First In First Out approach which makes it more suitable for searching vertices closer to the given source.
    - Time complexity : O(V + E).
    - Space complexity is more critical as compared to time complexity.
    - In BFS there is no concept of backtracking. 
    - BFS is optimal for finding the shortest path.
    - BFS is slow as compared to DFS because it explores nodes in all directions.

```
Pseudo code:

Queue: [start]
while:
    Dequeue:
    Is this the goal?
    If so, we are done
    Else, enqueue undiscovered neighbours and update predecessors
Repeat until the queue is empty
```


2. Depth First Search(DFS)
    - Stack data structure.
    - DFS uses Last In First Out approach which is more suitable when there are solutions away from source.
    - Time complexity : O(V + E).
    - DFS has lesser space complexity.
    - DFS is not optimal for finding the shortest path.
    - DFS algorithm is a recursive algorithm that uses the idea of backtracking.

```
Pseudo code:

Stack: [start]
While:
    Pop the stack:
    Is this the goal?
    If so, we are done
    Else, push undiscovered neighbours and update predecessors
Repeat until the stack is empty
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages.

```bash
pip install numpy matplotlib
```

## Running the scripts

* Available Mazes:
    - maze1, maze2, maze3, maze4, maze5, maze6

* Available Algorithms:
    - bfs     - Breadth First Search.
    - dfs     - Depth First Search.

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

To run the mazes which has multiple start of exit positions, user has to choose the location by typing the chosen option.

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

## Failure cases:
1. This robot will not get out of random maze without a given goal pose.
2. Real robot might not follow the given path and commands due to non holonomic constraints.

## Examples:

Color coding of following examples:

* White - Empty space
* Black - Obstacle boundary
* Red   - Start Pose 
* Green - Final path 
* Blue  - End Pose


1. Detecting empty space.

![](/images/maze0.png)

2. Walk through a “hallway” maze.

![](/images/maze2.png)

3. Find a way into and out of rooms.

![](/images/maze3.png)

4. Follow winding paths.

![](/images/maze4.png)

5. Reach the end of the maze which has multiple start points.

![](/images/maze5_a.png)

5. Reach the end of the maze which has multiple start points.

![](/images/maze5_b.png)

7. Reach the end of the maze which has dead ends.

![](/images/maze6.png)




# Part 2 : Reflection/Analysis

## Moving a 1x3 “ship” through a maze

![](/images/maze7.png)


A naive approach to solve this problem statement would be to hardcode behavior of the ship with multiple conditions and interlocks to execute that particular condition on the ship to get to the goal pose, however this is a very environment specific solution and would not generalize well.

So I described a generalized approach to solve this this problem statement in following steps 

## Assumptions:
- Start and goal pose will be selected by user. The robot will not get out of random maze without a given goal pose.

- Robot can follow the given path and commands

## Approach:

### Step 1: 
- Generate sample Mazes with the obstacles and tight spaces for the ship so that it has to perform different maneuvers – turn,move backward to reach valid exit.

- The mazes should be of increasing difficulty level, starting from the simple maze with straight path to involving tight turns and dead ends.


### Step 2:
- Implement a point robot solver for the maze, and to get better performance implement a heuristic based algorithm like A*

### Step 3:
- Build a visualization function which will help us check the performance of the the algorithm on mazes.

### Step 4: 
- Make the robot ship of three pixels to move through the simple straight line passage,without considering turns. 
All three pixels should move together 

### Step 5:
- Add collision constraints of robot by defining configuration space  and creating visibility graph.

- Following type of collision checking methods are used for mobile robots :
    - Geometric method
        - Scalar distance
    - Occupancy grid
        - Quadtree (2D maze)
        - Octree (3D maze)
    - Bounding volume hierarchies 

- To keep it simple for our ship, we can use a geometric method of scalar distance. In  this method we define obstacle exclusion zone as a simple geometric shaped zone around robot, and estimate the robot as a circular area and any obstacle overlapping on this area would be considered as a collision.

- Defining a circular shaped obstacle exclusion zone  is computationally efficient and easy to model but here the collision zone is larger which will detect walls as an obstacle even when there is sufficient space available, this is inefficient encapsulation.
- So, we can make a tradeoff and define a rectangular shaped obstacle exclusion zone which will work well in tight spaces.

- For Geometric methods, an important requirement is specific type of environment models and structures e.g.  The maze can be described by the points and lines to make the geometric methods of scalar distance. 

- The performance is a limiting factor for the complex environments, we might end up having way too many elements to check and could miss tight spaces.

- Using this collision check function we can test it on simple mazes with straight paths and obstacles to stop robot  



### Step 6: 

- Add Kinematic constraints to the ship.

- For some parts of maze we need to rotate ship along its center axis, so model of ship could be defined by the differential drive robot which is commonly used in robotics applications

- In the differential drive robot model we can control the wheels of the robot independently, by moving right and left wheels in opposite directions to turn the robot at its center axis.

- We need to consider following parameters 
    -   (x,y) Robots location like our previous pixel robot
    -   L - Wheelbase, 
    -   r - Radius of robot wheel 
    -   θ - Angle where the robot is heading.

The following equations will help us define the model of robot:

![](/images/differencial_drive.png)

     Differential Drive Model  [1]

![](/images/dd_equation.png)

     Differential Drive Equations  [1]

ur, ul =  angular wheel velocities 


### Step 7:

Implement an hybrid A* algorithm which will consider non holonomic constraints of robot motion and our model as differential drive. 

Hybrid A* will use the collision function we created to plan rotation condition check. 

- Previously implemented A* produces discontinuous path, which might not be traversable for the ship with kinematic constraints, so here we implement Hybrid A* [2] , a variant of the A* algorithm.

- Hybrid A* considers the vehicles dynamics and gives smooth path which could be followed by vehicle

- Given data for the algorithm
    - (x,y,θ) : Start
    - (x,y,θ) : Exit
    - 3 pixels : Length 

- Input Steering angles= [-45, 0 ,45]

    More values could be given for better exploration of nodes however this will increase the number of nodes to explore and slow down the exploration. 

- Input velocities. -1, 1


- We get six combinations (three for each forwards and backward direction) from above inputs which will be explored in algorithm.

    - [(-1,-45), (-1,0), (-1,45), (1,-45), (1,0), (1,45)]


        ![](/images/directions.png)


- Additional cost =[ 0.3, 0.1,0.3,0.05,0,0.05]

    These are to penalize the direction decisions.
First 3 values are greater than the later because we want to penalize backward direct paths more so that planner would  prefer forward direction paths.


- Vehicle dynamics model:

```
θ(t) = θ(t-1)+ v/L * tan(delta)
X(t) = X(t-1) v * cos(θ)
Y(t) = Y(t-1) v * sin(θ)
```

This describes changes in  X, Y, θ as a function of time. 

- We are computing position and angular orientation of vehicle, by considering values at previous time instance.

- This algorithm takes length of robot in consideration so the  3*3 space needed for the robot ship will be accounted by the algorithm.


### Step 8: 
- Check the robot performance on multiple turns and complex mazes with multiple obstacles and update code accordingly.

## Conclusion:

In this assessment, I implemented an algorithm approach to solve the given problem statement. The solution developed in the coding part is for the pixel robot, multiple algorithms could be implemented as per the situation e.g. Dijkstra, A*, however, to keep it simple I implemented Breadth-first search and Depth First Search algorithms.,
For part 2 consist of developing a solution for the real robot which is modelled in 2D space, for that I brainstormed multiple solutions however an approach which considers the model of the robot will generalize best for the same structure mazes. 
Path planning problem statements are fun to solve as we can directly check performance on visualization.
Thank you [Path Robotics](https://www.path-robotics.com/) for the opportunity to work on this problem statement.



## References : 

-  [Planning Algorithms and Differential Models](http://lavalle.pl/planning/ch13.pdf)

- [Hybrid A* ](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8702779)
