# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:35:19 2021

@author: guobr
"""
#  File: Graph.py

#  Description:

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/30

#  Date Last Modified: 4/30

import sys

class Stack (object):
  def __init__(self):
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

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))

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

class Edge(object):
    def _init__(self, vert1, vert2, weight):
        self.fromvert = vert1
        self.tovert = vert2
        self.weight = weight
    
    
class Graph (object):
    
  def __init__ (self):
    self.Vertices = []          # list of Vertex objects
    self.adjMat = []            # adjacency matrix
    self.edges = []
    
  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given a label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (not self.has_vertex(label)):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append(0)

      # add a new row for the new Vertex
      new_row = []
      for i in range (nVert):
        new_row.append (0)
      self.adjMat.append (new_row)

  # add weighted directed edge to the graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to the graph
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

  # do the depth first search in a graph
  def dfs (self, v):
    # create the Stack object
    theStack = Stack()

    # mark the vertex v as visited and push it on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first seach in the graph
  def bfs (self, v):
    # create a Queue object
    theQueue = Queue()
    # mark v as visited, print it and enqueue it
    self.Vertices[v].visited = True
    print(self.Vertices[v])
    theQueue.enqueue(v)
    # print each value in queue until there are no more vertices in the queue
    while not theQueue.is_empty():
        v1 = theQueue.dequeue()
        v2 = self.get_adj_unvisited_vertex(v1)
        # as long as vertice exists, print and enqueue it
        while v2 != -1:
            self.Vertices[v2].visited = True
            print(self.Vertices[v2])
            theQueue.enqueue(v2)
            v2 = self.get_adj_unvisited_vertex(v1)
            
    # the queue is empty, so we reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight (self, fromVertexLabel, toVertexLabel):
      weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
      if weight == 0:
          return -1
      return weight
          

  # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors (self, vertexLabel):
      neighbors = []
      indx = self.get_index(vertexLabel)
      for i in range(len(self.Vertices[indx])):
          if self.Vertices[indx][i] != 0:
              neighbors.append(self.Vertices[indx][i])
      return neighbors


  # get a copy of the list of Vertex objects
  def get_vertices (self):
      ans = []
      for i in range(len(self.Vertices)):
          ans.append(self.Vertices[i])
      return ans
          

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    # get index of the two vertexs' whose edge will be delted
      fromIndex = self.get_index(fromVertexLabel)
      toIndex = self.get_index(toVertexLabel)
      # delete adjacencies/ edge
      self.adjMat[fromIndex][toIndex] = 0
      self.adjMat[toIndex][fromIndex] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
      # get the index of the vertex to be deleted
      indx = self.get_index(vertexLabel)
      # pop it and deleted adjacencies
      self.Vertices.pop(indx)
      del self.adjMat[indx]
      for i in range(len(self.Vertices)):
          del self.adjMat[i][indx]

def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)

  # do the depth first search
  print ("Depth First Search")
  cities.dfs (start_index)
  print ()
  
  print('Breadth First Search')
  cities.bfs(start_index)
  print()

  print()
  print('Adjacency Matrix')
  for i in range(num_vertices):
    for j in range(num_vertices):
        if j != num_vertices - 1:
            print(cities.adjMat[i][j], end = " ")
        else:
            print(cities.adjMat[i][j], end = "")
    print()
  print()
  
  # test deletion of an edge
  print('Deletion of an edge')
  twocities = sys.stdin.readline().strip()
  twocities = twocities.split()
  cities.delete_edge(twocities[0], twocities[1])

  print()
  print('Adjacency Matrix')
  for i in range(num_vertices):
    for j in range(num_vertices):
        if j != num_vertices - 1:
            print(cities.adjMat[i][j], end = " ")
        else:
            print(cities.adjMat[i][j], end = "")
    print()
  print()

  # test deletion of a vertex
  print('Deletion of a vertex')
  toDel = sys.stdin.readline().strip()
  cities.delete_vertex(toDel)
  num_vertices -= 1
  print()
  print('List of Vertices')

  for vertice in cities.Vertices:
    print(vertice)

  print()
  print('Adjacency Matrix')

  for i in range(num_vertices):
    for j in range(num_vertices):
        if j != num_vertices - 1:
            print(cities.adjMat[i][j], end = " ")
        else:
            print(cities.adjMat[i][j], end = "")
    print()
  print()
    
if __name__ == "__main__":
  main()