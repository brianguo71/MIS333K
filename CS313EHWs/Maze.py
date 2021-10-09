#  File: Maze.py

#  Description: Determine if you can escape the maze

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

import sys

# determines whether we can escape this maze with k energy
# returns a Boolean
def solve(maze, energy):
    energy -= maze[0][0]
    x = 0
    y = 0
    while energy > 0 and (len(maze[0])-1) != x:
        if maze[y + 1][x] < maze[y][x + 1]:
            energy -= maze[y+1][x]
        else:
            energy -= maze[y][x+1]
        energy -= maze[y+1][x+1]
        x += 1
        y += 1
    if (len(maze[0]) - 1) == x and energy >= 0:
        return True
    return False


def main():
    # read in N (maze size)
    N = int(sys.stdin.readline().strip())
 
    # read in K (amount of energy)
    energy = int(sys.stdin.readline().strip())
 
    # read in the maze
    maze = [[0 for i in range(N)] for k in range(N)]
    for i in range(N):
        line = sys.stdin.readline().strip().split(" ")
        for k in range(N):
            maze[i][k] = int(line[k])
 
    # determine if the maze can be escaped
    if solve(maze, energy):
        print("ESCAPED")
    else:
        print("TRAPPED")
 
if __name__ == "__main__":
    main()