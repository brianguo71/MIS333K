# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:52:27 2021

@author: guobr
"""


#  File: Triangle.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    ans = []
    brutehelper(grid, len(grid), 1, grid[0][0], 0, ans)
    ans.sort()
    return ans[-1]


def brutehelper(grid, i, curr, runningsum, l, ans):
    if curr == i:
        ans.append(runningsum)
    else:
        b = brutehelper(grid, i, curr + 1, runningsum + grid[curr][l], l, ans)
        c = brutehelper(grid, i, curr + 1, runningsum + grid[curr][l + 1], l+1, ans)


        

# returns the greatest path sum using greedy approach
def greedy (grid):
    j = grid[0][0]
    l = 0
    for i in range(1,len(grid)):
        a = grid[i][l]
        b = grid[i][l + 1]
        if a > b:
            j += a
        else:
            j += b
            l += 1

    
    return j

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
        
    return dividehelper(grid, len(grid), 1, grid[0][0], 0)

def dividehelper(grid, i, curr, runningsum, l):
    if curr == i:
        return runningsum
    b = dividehelper(grid, i, curr + 1, runningsum + grid[curr][l], l)

    c = dividehelper(grid, i, curr + 1, runningsum + grid[curr][l + 1], l+1)

    return max(b, c)
# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    for i in range(len(grid[0]) - 2, -1, -1):
        for j in range(i + 1):
            grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])
    return grid[0][0]

    
    
# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The greatest path sum through exhaustive search is')
  print(brute_force(grid))
  print('The time taken for exhaustive approach in seconds is')
  print(times)

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The greatest path sum through greedy search is')
  print(greedy(grid))
  print('The time taken for greedy approach in seconds is')
  print(times)

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The greatest path sum through recursive search is')
  print(divide_conquer(grid))
  print('The time taken for recursive approach in seconds is')
  print(times)
  
  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The greatest path sum through dynamic programming is')
  print(dynamic_prog(grid))
  print('The time taken for dynamic programming in seconds is')
  print(times)

if __name__ == "__main__":
  main()
