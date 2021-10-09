# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:15:24 2021

@author: guobr
"""
#  File: Boxes.py

#  Description: Given some amount of boxes, return the maximum number of boxes
#               that fit within each other and the number of such boxes that fit

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number:  52230

#  Date Created: 3/26/21

#  Date Last Modified: 3/26/21

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# Input:
# 	box_list is a list of boxes that have already been sorted
# 	sub_set is a list that is the current subset of boxes
# 	idx is an index in the list box_list
# 	all_box_subsets is a 3-D list that has all the subset of boxes
# Output:
#		Nothing should be returned (None)
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    #base case (idx == len(box_list)) is at the end of box_list
    if (idx == len(box_list)):
        all_box_subsets.append(sub_set)
    else:
        diffset = sub_set[:]
        sub_set.append(box_list[idx])
        #use recursive backtracking to create every possible subset of boxes
        sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
        sub_sets_boxes(box_list, diffset, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
# Input: 
#   all_box_subsets: list containing every subset of boxes
# Output: 
#		return a list containing all largest nesting subsets 
# 	i.e. if multiple nesting subsets are of size 4 (and 4 is the largest size),
# 	the list MUST contain both subsets
def largest_nesting_subsets (all_box_subsets):
    largestsize = 0
    ans = []
    #check every subset
    for i in all_box_subsets:
        if len(i) >= largestsize:
            #flag variable
            nested = True
            for j in range(len(i)-1):
                #if any boxes within the subset do not nest, we set our 'nested'
                #flag as False to not add this subset to the ans list
                if does_fit(i[j], i[j + 1]) == False:
                    nested = False
            if nested:
                ans.append(i)
                largestsize = len(i)
                #use recheck helper method to remove smaller subsets
                ans = recheck(ans, largestsize)

            
    return ans

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


#used as a helper method for largest_nesting_subsets
#Input:
    #nestingsubsets: largest_nesting_subets' current largesting nesting subset
    #length: len of current subset being added to list of largest nesting subsets
#Output:
    #ans: largest_nesting_subset after getting rid of all subsets smaller than
    #the current subset being added
def recheck(nestingsubsets, length):
    ans = []
    for i in nestingsubsets:
        if len(i) >= length:
            ans.append(i)
    return ans

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)


  # print the largest number of boxes that fit
  print(len(all_nesting_boxes[0]))

  # print the number of sets of such boxes
  print(len(all_nesting_boxes))

if __name__ == "__main__":
  main()
