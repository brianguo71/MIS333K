# -*- coding: utf-8 -*-
"""
Created on Mon May  3 08:26:59 2021

@author: guobr
"""
#  File: TopoSort.py

#  Description: Create a topological sort method and a method to check if
#  a given directional graph is a cycle

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 5/3/21

#  Date Last Modified: 5/3/21

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))
  
  # return whether stack contains a given element
  def contains(self, element):
    all_elements = []
    while self.is_empty() == False:
      all_elements.append(self.pop())
    all_elements.reverse()
    for ele in all_elements:
      self.push(ele)
    if (element in all_elements):
      return True
    return False


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  
  def delete_vertex (self, vertexLabel):
      # get the index of the vertex to be deleted
      indx = self.get_index(vertexLabel)
      # pop it and deleted adjacencies
      self.Vertices.pop(indx)
      del self.adjMat[indx]
      for i in range(len(self.Vertices)):
          del self.adjMat[i][indx]

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
    # go through each vertice to check if a graph cycles
    nVert = len (self.Vertices)

    # do a depth first search for each vertice
    for v in range(nVert):
      # create the Stack object
      theStack = Stack()

      # mark vertex v as visited and push it on the stack
      (self.Vertices[v]).visited = True
      theStack.push (v)

      # visit the other vertices according to depth
      while (not theStack.is_empty()):
        # get an adjacent unvisited vertex
        u = self.has_cycle_adj (theStack)

        if (u == -1): 
          u = theStack.pop()

        # returns true if our has_cycle_adj returns -2
        # returns -2 when a vertice completes a cycle
        elif (u == -2):
          nVert = len (self.Vertices)
          for i in range (nVert):
            (self.Vertices[i]).visited = False
          return True
        else:
          (self.Vertices[u]).visited = True
          theStack.push(u)
      # the stack is empty let us reset the flags
      nVert = len (self.Vertices)
      for i in range (nVert):
        (self.Vertices[i]).visited = False
    
    # return False after checking for cycle
    return False
  
  # adj method updated to also return -2 if vertice completes a cycle
  def has_cycle_adj(self, stack):
    nVert = len(self.Vertices)
    v = stack.peek()
    for i in range (nVert):
      if (self.adjMat[v][i] > 0 and (self.Vertices[i]).was_visited()):
        if (stack.contains(i)):
          return -2
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1


  #return a list of vertices after a topological sort
  #this function should not print the list
  def toposort(self):
    # create a Queue
    theQueue = Queue()
    # until the graph is empty / all vertices have been added to our list,
    # only add in values who no adjacencies
    while self.adjMat != []:
      nVert = len(self.Vertices)
      toDelete = []
      # for every vertice
      for end in range(nVert):
        # check if they have any adjacencies
        count = 0
        for start in range(nVert):
          if self.adjMat[start][end] == 0:
            count += 1
        # if they don't (count == nVert), add them to our Queue and delete them
        if count == nVert:
          theQueue.enqueue(self.Vertices[end].label)
          toDelete.append(self.Vertices[end])
      for vertice in toDelete:
        self.delete_vertex(vertice.label)

    return theQueue.queue



def main():
  # create a Graph object
  theGraph = Graph()
  
  numlines = int((sys.stdin.readline()).strip())
  
  for i in range(numlines):
      line = (sys.stdin.readline()).strip()
      theGraph.add_vertex(line)
      
  numedges = int((sys.stdin.readline()).strip())
  
  for i in range(numedges):
      line = (sys.stdin.readline()).strip()
      line = line.split()
      start = theGraph.get_index(line[0])
      end = theGraph.get_index(line[1])
      theGraph.add_directed_edge(start, end)

  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
      print ("The Graph has a cycle.")
  else:
      print ("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)

    
if __name__ == "__main__":
  main()
