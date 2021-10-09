# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:06:27 2021

@author: guobr
"""
#  File: Geometry.py

#  Description: Point, sphere, cube and cylinder objects

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 2/12/21

#  Date Last Modified: 2/12/21

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = float(x)
      self.y = float(y)
      self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return '({:.1f}, {:.1f}, {:.1f})'.format(self.x, self.y, self.z)

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) **2) ** 0.5

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 1.0e-6
      return ((abs(self.x - other.x)) < tol) and ((abs(self.y - other.y) < tol)) and ((abs(self.z - other.z)) < tol)
      

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.center = Point(x, y, z)
      self.radius = float(radius)
      self.x = float(x)
      self.y = float(y)
      self.z = float(z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      return 'Center: ({:.1f}, {:.1f}, {:.1f}), Radius: {:.1f}'.format(self.center.x, self.center.y, self.center.z, self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      area = 4 * math.pi * self.radius ** 2
      return area

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      volume = 4/3 * math.pi * self.radius **3
      return volume

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return (self.center.distance(p)) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      distbetween_centers = self.center.distance(other.center)
      return (distbetween_centers + other.radius) < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      return self.is_inside_point(a_cube.corner1) and self.is_inside_point(a_cube.corner2) \
          and self.is_inside_point(a_cube.corner3) and self.is_inside_point(a_cube.corner4) \
              and self.is_inside_point(a_cube.corner5) and self.is_inside_point(a_cube.corner6) \
                  and self.is_inside_point(a_cube.corner7) and self.is_inside_point(a_cube.corner8)

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      return self.is_inside_point(a_cyl.corner1) and self.is_inside_point(a_cyl.corner2) \
          and self.is_inside_point(a_cyl.corner3) and self.is_inside_point(a_cyl.corner4) \
              and self.is_inside_point(a_cyl.corner5) and self.is_inside_point(a_cyl.corner6) \
                  and self.is_inside_point(a_cyl.corner7) and self.is_inside_point(a_cyl.corner8)
      
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
      distancebetween = self.center.distance(other.center)
      isstrictlyoutside = distancebetween > (self.radius + other.radius)
      return not(isstrictlyoutside or self.is_inside_sphere(other))

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean        
  def does_intersect_cube (self, a_cube):
      return not(self.cubeStrictlyOutside(a_cube) or self.is_inside_cube(a_cube))
  
  # determines if a cube is strictly outside this Sphere
  # returns a Boolean
  def cubeStrictlyOutside(self, a_cube):
      return not(self.is_inside_point(a_cube.corner1) or self.is_inside_point(a_cube.corner2) \
          or self.is_inside_point(a_cube.corner3) or self.is_inside_point(a_cube.corner4) \
              or self.is_inside_point(a_cube.corner5) or self.is_inside_point(a_cube.corner6) \
                  or self.is_inside_point(a_cube.corner7) or self.is_inside_point(a_cube.corner8))

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      cubeA = Cube(self.x, self.y, self.z, (2*self.radius)/(3**0.5))
      return cubeA
     


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.center = Point(x, y, z)
      self.side = float(side)
      self.l = float(side)/2
      self.corner1 = Point(float(x) - self.l, float(y) + self.l, float(z) - self.l)
      self.corner2 = Point(float(x) + self.l, float(y) + self.l, float(z) - self.l)
      self.corner3 = Point(float(x) - self.l, float(y) - self.l, float(z) - self.l)
      self.corner4 = Point(float(x) + self.l, float(y) - self.l, float(z) - self.l)
      self.corner5 = Point(float(x) - self.l, float(y) + self.l, float(z) + self.l)
      self.corner6 = Point(float(x) + self.l, float(y) + self.l, float(z) + self.l)
      self.corner7 = Point(float(x) - self.l, float(y) - self.l, float(z) + self.l)
      self.corner8 = Point(float(x) + self.l, float(y) - self.l, float(z) + self.l)
      

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      return 'Center: ({:.1f}, {:.1f}, {:.1f}), Side: {:.1f}'.format(self.center.x, self.center.y, self.center.z, self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      return 6 * self.side ** 2

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      return self.side ** 3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      return self.center.x - self.l < p.x < self.center.x + self.l and\
          self.center.y - self.l < p.y < self.center.y + self.l and\
              self.center.z - self.l < p.z < self.center.z + self.l

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      cubeSphere = Cube(a_sphere.center.x, a_sphere.center.y, a_sphere.center.z, a_sphere.radius*2)
      return self.is_inside_cube(cubeSphere)
      

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      return self.is_inside_point(other.corner1) and self.is_inside_point(other.corner2)\
          and self.is_inside_point(other.corner3) and self.is_inside_point(other.corner4)\
              and self.is_inside_point(other.corner5) and self.is_inside_point(other.corner6)\
                  and self.is_inside_point(other.corner7) and self.is_inside_point(other.corner8)
              

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      return self.is_inside_point(a_cyl.corner1) and self.is_inside_point(a_cyl.corner2)\
          and self.is_inside_point(a_cyl.corner3) and self.is_inside_point(a_cyl.corner4)\
              and self.is_inside_point(a_cyl.corner5) and self.is_inside_point(a_cyl.corner6)\
                  and self.is_inside_point(a_cyl.corner7) and self.is_inside_point(a_cyl.corner8)

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
      return not(self.strictly_outside(other) or self.is_inside_cube(other))


  # determines if another Cube is strictly outside this cube
  def strictly_outside(self, a_cube):
      return not(self.is_inside_point(a_cube.corner1) or self.is_inside_point(a_cube.corner2) \
          or self.is_inside_point(a_cube.corner3) or self.is_inside_point(a_cube.corner4) \
              or self.is_inside_point(a_cube.corner5) or self.is_inside_point(a_cube.corner6) \
                  or self.is_inside_point(a_cube.corner7) or self.is_inside_point(a_cube.corner8))
          
  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
      volume = min(self.corner2.x,other.corner2.x)-max(self.corner1.x,other.corner1.x) * min(self.corner2.y,other.corner2.y)-max(self.corner1.y,other.corner1.y) * min(self.corner2.z,other.corner2.z)-max(self.corner1.z,other.corner1.z)
      return volume
  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
      aSphere = Sphere(self.center.x, self.center.y, self.center.z, radius = self.side/2)
      return aSphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.center = Point(x, y, z)
      self.radius = float(radius)
      self.height = float(height)
      self.corner1 = Point(float(x) - float(radius), float(y) + float(radius), float(z) - float(height)/2)
      self.corner2 = Point(float(x) + float(radius), float(y) + float(radius), float(z) - float(height)/2)
      self.corner3 = Point(float(x) - float(radius), float(y) - float(radius), float(z) - float(height)/2)
      self.corner4 = Point(float(x) + float(radius), float(y) - float(radius), float(z) - float(height)/2)
      self.corner5 = Point(float(x) - float(radius), float(y) + float(radius), float(z) + float(height)/2)
      self.corner6 = Point(float(x) + float(radius), float(y) + float(radius), float(z) + float(height)/2)
      self.corner7 = Point(float(x) - float(radius), float(y) - float(radius), float(z) + float(height)/2)
      self.corner8 = Point(float(x) + float(radius), float(y) - float(radius), float(z) + float(height)/2)
      self.x = float(x)
      self.y = float(y)
      self.z = float(z)

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return 'Center: ({:.1f}, {:.1f}, {:.1f}), Radius: {:.1f}, Height: {:.1f}'.format(self.center.x, self.center.y, self.center.z, self.radius, self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      return math.pi * self.radius ** 2 * self.height

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      xyplanepoint = Point(self.x, self.y, 0)
      return  self.center.z - self.height/2 < p.z < self.center.z + self.height/2 and\
          xyplanepoint.distance(Point(p.x,p.y,0)) < self.radius

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      newcube = a_sphere.circumscribe_cube()
      return self.is_inside_cube(newcube)
      

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      return self.is_inside_point(a_cube.corner1) and self.is_inside_point(a_cube.corner2)\
          and self.is_inside_point(a_cube.corner3) and self.is_inside_point(a_cube.corner4)\
              and self.is_inside_point(a_cube.corner5) and self.is_inside_point(a_cube.corner6)\
                  and self.is_inside_point(a_cube.corner7) and self.is_inside_point(a_cube.corner8)
      

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
      return self.is_inside_point(other.corner1) and self.is_inside_point(other.corner2)\
          and self.is_inside_point(other.corner3) and self.is_inside_point(other.corner4)\
              and self.is_inside_point(other.corner5) and self.is_inside_point(other.corner6)\
                  and self.is_inside_point(other.corner7) and self.is_inside_point(other.corner8)

  # determines if another Cylinder is strictly outside this Cylinder
  def isStrictlyOutside(self, other):
      xydummy1 = Point(self.x, self.y, 0)
      xydummy2 = Point(other.x, other.y, 0)
      return xydummy1.distance(xydummy2) >= (self.radius + other.radius) or\
          abs(self.z - other.z) >= (0.5*(self.height + other.height))
          
  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
      return not(self.isStrictlyOutside(other) or self.is_inside_cylinder(other))

def main():
  # read data from standard input
  
  # read the coordinates of the first Point p
  Pdata = sys.stdin.readline().strip()
  # create a Point object 
  pval = Pdata.split()
  P = Point(pval[0], pval[1], pval[2])
  # read the coordinates of the second Point q
  Qdata = sys.stdin.readline().strip()
  # create a Point object 
  qval = Qdata.split()
  Q = Point(qval[0], qval[1], qval[2])
  
  # read the coordinates of the center and radius of sphereA
  sphereAdata = sys.stdin.readline().strip()
  # create a Sphere object 
  sphereAval = sphereAdata.split()
  sphereA = Sphere(sphereAval[0], sphereAval[1], sphereAval[2], sphereAval[3])
  
  # read the coordinates of the center and radius of sphereB
  sphereBdata = sys.stdin.readline().strip()
  # create a Sphere object
  sphereBval = sphereBdata.split()
  sphereB = Sphere(sphereBval[0], sphereBval[1], sphereBval[2], sphereBval[3])

  # read the coordinates of the center and side of cubeA
  cubeAdata = sys.stdin.readline().strip()
  # create a Cube object 
  cubeAval = cubeAdata.split()
  cubeA = Cube(cubeAval[0], cubeAval[1], cubeAval[2], cubeAval[3])
  
  # read the coordinates of the center and side of cubeB
  cubeBdata = sys.stdin.readline().strip()
  # create a Cube object 
  cubeBval = cubeBdata.split()
  cubeB = Cube(cubeBval[0], cubeBval[1], cubeBval[2], cubeBval[3])
  
  # read the coordinates of the center, radius and height of cylA
  cylAdata = sys.stdin.readline().strip()
  # create a Cylinder object 
  cylAval = cylAdata.split()
  cylA = Cylinder(cylAval[0], cylAval[1], cylAval[2], cylAval[3], cylAval[4])
  
  # read the coordinates of the center, radius and height of cylB
  cylBdata = sys.stdin.readline().strip()
  # create a Cylinder object
  cylBval = cylBdata.split()
  cylB = Cylinder(cylBval[0], cylBval[1], cylBval[2], cylBval[3], cylBval[4])

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  origin = Point(0,0,0)
  if P.distance(origin) > Q.distance(origin):
      print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
  else:
      print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

  # print if Point p is inside sphereA
  if sphereA.is_inside_point(P):
      print('Point p is inside sphereA')
  else:
      print('Point p is not inside sphereA')
      
  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB):
      print('sphereB is inside sphereA')
  else:
      print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
  if sphereA.is_inside_cube(cubeA):
      print('cubeA is inside sphereA')
  else:
      print('cubeA is not inside sphereA')
  # print if cylA is inside sphereA
  if sphereA.is_inside_cyl(cylA):
      print('cylA is inside sphereA')
  else:
      print('cylA is not inside sphereA')
  # print if sphereA intersects with sphereB
  if(sphereA.does_intersect_sphere(sphereB)):
      print('sphereA does intersect sphereB')
  else:
      print('sphereA does not intersect sphereB')
  # print if cubeB intersects with sphereB
  if(sphereB.does_intersect_cube(cubeB)):
      print('cubeB does intersect sphereB')
  else:
      print('cubeB does not intersect sphereB')
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  sphereAcube = sphereA.circumscribe_cube()
  if sphereAcube.volume() > cylA.volume():
      print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
      print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  # print if Point p is inside cubeA
  if cubeA.is_inside_point(P):
      print('Point p is inside cubeA')
  else:
      print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA):
      print('sphereA is inside cubeA')
  else:
      print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB):
      print('cubeB is inside cubeA')
  else:
      print('cubeB is not inside cubeA')
  # print if cylA is inside cubeA
  if cubeA.is_inside_cylinder(cylA):
      print('cylA is inside cubeA')
  else:
      print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB):
      print('cubeA does intersect cubeB')
  else:
      print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cubeA.intersection_volume(cubeB) > sphereA.volume():
      print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
      print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')
  
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  cubeAsphere = cubeA.inscribe_sphere()
  if cubeAsphere.area() > cylA.area():
      print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
      print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')

  # print if Point p is inside cylA
  if cylA.is_inside_point(P):
      print('Point p is inside cylA')
  else:
      print('Point p is not inside cylA')
  # print if sphereA is inside cylA
  if cylA.is_inside_sphere(sphereA):
      print('sphereA is inside cylA')
  else:
      print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
  if cylA.is_inside_cube(cubeA):
      print('cubeA is inside cylA')
  else:
      print('cubeA is not inside cylA')
  # print if cylB is inside cylA
  if cylA.is_inside_cylinder(cylB):
      print('cylB is inside cylA')
  else:
      print('cylB is not inside cylA')
  # print if cylB intersects with cylA
  if cylA.does_intersect_cylinder(cylB):
      print('cylB does intersect cylA')
  else:
      print('cylB does not intersect cylA')

if __name__ == "__main__":
  main()


