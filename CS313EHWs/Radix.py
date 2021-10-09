# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:22:25 2021

@author: guobr
"""
#  File: Radix.py

#  Description: Create a implementation of radix sort that can sort strings 
#  containing both integers(0-9) and letters (a-z)

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 55230

#  Date Created: 4/6/21

#  Date Last Modified: 4/6/21

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # creates a dictionary that gives us the priority of each character in a sort
  # ex: 0 would be before 1 and a would be before b
  sortdict = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6,
              '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14,
              'f':15, 'g':16, 'h':17, 'i':18, 'j': 19, 'k': 20, 'l': 21, 'm': 22
              , 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r' : 27, 's': 28, 't': 29,
              'u': 30, 'v': 31, 'w' :32, 'x':33, 'y':34, 'z' :35, '*': 0}
  
  # creates 36 queues (one for each character possible)
  queues = []
  for i in range(36):
      queues.append(Queue())

  # find the length of the longest string in our list
  # this value is the number of passes our sorting algorithm will do
  maxlen = len(max(a, key = len))

  # for strings in our list that are shorter than the longest string,
  # we add '*'s to the end until each string in the list is of matching length
  for strngi in range(len(a)):
      while len(a[strngi]) < maxlen:
          a[strngi] = a[strngi] + '*'

  
  for passnum in range(maxlen):
      # queue each string in our list into queues based upon the character
      # at passnum indexes away from the end of the string
      for strng in a:
          queueindex = sortdict[strng[len(strng) - passnum - 1]]
          (queues[queueindex]).enqueue(strng)


      # update our list by dequeueing every value and adding them to a new list
      newa = []
      for indx in range(36):
          while queues[indx].is_empty() == False:
              newa.append(queues[indx].dequeue())
      a = newa
      
  # remove every '*' and return the now sorted list
  ans = []
  for strng in a:
      ans.append(strng.replace('*', ""))

  return ans

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    