# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:57:05 2021

@author: guobr
"""

#  File: OfficeSpace.py

#  Description: Allocate office space according to cubicle requests

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number:  52230

#  Date Created: 2/13/21

#  Date Last Modified: 2/13/21

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    ans = (0, 0, 0, 0)
    if (rect2[1] > rect1[3] or rect2[0] > rect1[2]) or\
        (rect1[1] > rect2[3] or rect1[0] > rect2[2]):
            return ans
    else:
        ans = (max(rect1[0], rect2[0]), max(rect1[1], rect2[1]), min(rect1[2], rect2[2]), min(rect1[3], rect2[3]))
        return ans

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    unallocated = 0
    for x in range(len(bldg)):
        for y in range(len(bldg[x])):
            if bldg[x][y] == 0:
                unallocated += 1
    return unallocated
            

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    contested = 0
    for x in range(len(bldg)):
        for y in range(len(bldg[x])):
            if bldg[x][y] > 1:
                contested += 1
    return contested
    

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    uncontested = 0
    for x in range(rect[0],rect[2]):
        for y in range(rect[1], rect[3]):
            if bldg[y][x] <= 1:
                uncontested += 1
    return uncontested
            

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    office2d = [[0 for i in range(office[2])] for j in range(office[3])]
    for eachcubicle in cubicles:
        for x in range(eachcubicle[0], eachcubicle[2]):
            for y in range(eachcubicle[1], eachcubicle[3]):
                office2d[y][x] += 1
    return office2d

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
  # read the data
  wh = sys.stdin.readline().strip()
  whlist = wh.split()
  office = (0, 0, int(whlist[0]), int(whlist[1]))
  numpeople = int(sys.stdin.readline().strip())
  namelist = []
  cubelist = []
  for i in range(numpeople):
      requestdry = sys.stdin.readline().strip()
      rdata = requestdry.split()
      name = rdata[0]
      cubiclerequested = (int(rdata[1]), int(rdata[2]), int(rdata[3]), int(rdata[4]))
      namelist.append(name)
      cubelist.append(cubiclerequested)
      
  office2d = request_space(office, cubelist)
  # run your test cases
  '''
  print (test_cases())
  '''

  # print the following results after computation
  
  # compute the total office space
  print('Total', area(office))
  # compute the total unallocated space
  print('Unallocated', unallocated_space(office2d))
  # compute the total contested space
  print('Contested', contested_space(office2d))
  # compute the uncontested space that each employee gets
  for i in range(len(namelist)):
      print(namelist[i], uncontested_space(office2d, cubelist[i]))

if __name__ == "__main__":
  main()