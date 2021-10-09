# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:30:48 2021

@author: guobr
"""
#  File: Josephus.py

#  Description:  Creates a circular linked list and helper methods to solve
#  Josephus problem

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/12/21

#  Date Last Modified: 4/12/21

import sys

class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next


class CircularList(object):
  # Constructor
  def __init__ ( self ): 
      self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
      insert = Link(data)
      current = self.first
      
      # if circularlist is empty, add our element and link it to itself
      if current == None:
          self.first = insert
          insert.next = insert
          return
      
      # set current to last position
      while current.next != self.first:
          current = current.next
          
      current.next = insert
      insert.next = self.first

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
      current = self.first

      # go through each value in the list
      while current.next != self.first:
          # return current if there is a match or move onto next link if not
          if current.data == data:
              return current
          else:
              current = current.next
      if current.data == data:
          return current
      # returns None if there is never a match
      return None
          

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there

  def delete ( self, data ):
      current = self.first
      previous = self.first
      
      if current == None:
          return None
      
      # if data isn't in the list, return None
      if self.find(data) == None:
          return None
      
      # set previous to the last link in the circle
      while previous.next != self.first:
          previous = previous.next

      # if there is only 1 element in the circle, set that element to None
      if current.next == current:
                  self.first = None
                  return
      
      # if the first value is our data, set our circles first as the next value
      # and set our last link's next as our 2nd value
      if current.data == data:
          self.first = current.next
          previous.next = current.next
          return
      # iterate until current.data == data
      while current.data != data:
              previous = previous.next
              current = current.next
    
      previous.next = current.next
          

  # Delete the nth Link starting from the Link start 
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
      # set current at start
      current = self.find(start)
      # move n numbers down
      # >1 instead of 0 to count the first number
      while n > 1:
          current = current.next
          n -= 1
      # delete link and update previous link's next
      deleteddata = current.data
      nextlink = current.next
      self.delete(current.data)
      return (deleteddata, nextlink.data)
          

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__ 
  # format for normal Python lists
  def __str__ ( self ):
      current = self.first
      # return '[]' if circular list is empty
      if current == None:
          return '[]'
      
      # start with [
      ans = '['
      
      # go through entire list
      while current.next != self.first:
          # add each value
          ans += str(current.data)
          if current.next != self.first:
              # while the current value is not the last, add a coma + space
              ans += ', '
          current = current.next
      ans += str(current.data)
      # return each number followed by a ]
      return ans + ']'

def main():

  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # create a circular list and fill it with num of soldiers given starting at 1
  soldiers = CircularList()
  for soldier in range(1, num_soldiers + 1):
      soldiers.insert(soldier)
  
  # delete soldiers depending on elim_num
  for i in range(1, num_soldiers + 1):
      v = soldiers.delete_after(start_count, elim_num)
      print(v[0])
      start_count = v[1]

if __name__ == "__main__":
  main()