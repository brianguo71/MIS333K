# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:47:48 2021

@author: guobr
"""

#  File: Hull.py

#  Description: Create a convex hull that encloses a given set of points

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 3/1/2021

#  Date Last Modified: 3/1/2021

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
   d = (p.x * q.y) + (q.x * r.y) + (r.x * p.y) - (p.x * r.y) - (p.y * q.x) - (q.y * r.x)
   return d

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
   upper_hull = []
   upper_hull.append(sorted_points[0])
   upper_hull.append(sorted_points[1])
   for i in range(2, len(sorted_points)):
       upper_hull.append(sorted_points[i])
       p = upper_hull[len(upper_hull) - 3]
       q = upper_hull[len(upper_hull) - 2]
       r = upper_hull[len(upper_hull) - 1]
       while len(upper_hull) >= 3 and det(p, q, r) >= 0:
           upper_hull.pop(len(upper_hull) - 2)
           p = upper_hull[len(upper_hull) - 3]
           q = upper_hull[len(upper_hull) - 2]
           r = upper_hull[len(upper_hull) - 1]
   lower_hull = []
   lower_hull.append(sorted_points[len(sorted_points) - 1])
   lower_hull.append(sorted_points[len(sorted_points) - 2])
   for i in range(len(sorted_points) - 3, -1, -1):
       lower_hull.append(sorted_points[i])
       p = lower_hull[len(lower_hull) - 3]
       q = lower_hull[len(lower_hull) - 2]
       r = lower_hull[len(lower_hull) - 1]
       while len(lower_hull) >= 3 and det(p,q,r) >= 0:
           lower_hull.pop(len(lower_hull) - 2)
           p = lower_hull[len(lower_hull) - 3]
           q = lower_hull[len(lower_hull) - 2]
           r = lower_hull[len(lower_hull) - 1]

   lower_hull.pop(0)
   lower_hull.pop(len(lower_hull) - 1)
   convex_hull = []
   convex_hull.extend(upper_hull)
   convex_hull.extend(lower_hull)
           
   return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
   i = 0
   tot = 0
   while i < len(convex_poly) - 1:
       tot += (convex_poly[i].x * convex_poly[i + 1].y)
       tot -= (convex_poly[i].y * convex_poly[i + 1].x)
       i += 1
   tot += (convex_poly[0].y * convex_poly[i].x)
   tot -= (convex_poly[0].x * convex_poly[i].y)
   area = 0.5 * abs(tot)
   return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  chull = convex_hull(sorted_points)
  # run your test cases

  # print your results to standard output
  
  # print the convex hull
  print('Convex Hull')
  for i in range(len(chull)):
      px = chull[i].x
      py = chull[i].y
      print('({}, {})'.format(px,py))
  # get the area of the convex hull
  area = area_poly(chull)
  # print the area of the convex hull
  print()
  print('Area of Convex Hull =', area)
if __name__ == "__main__":
  main()