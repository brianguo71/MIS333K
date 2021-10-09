# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:19:42 2021

@author: guobr
"""
import sys
#  File: Intervals.py

#  Description: 

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 2/4/2021

#  Date Last Modified: 2/5/2021



# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the interval
def merge_tuples(tuplist):
    tuplist.sort(key=lambda x: x[0])
    i = 0
    cont = True
    while cont:
        if i == len(tuplist)-1:
            cont = False
        else:
            if tuplist[i+1][0] <= tuplist[i][1]:
                if tuplist[i][1] > tuplist[i+1][1]:
                    tuplist.pop(i+1)
                else:
                    tuplist[i] = (tuplist[i][0], tuplist[i+1][1])
                    tuplist.pop(i+1)
            else:
                i += 1
    return tuplist
    

#Input: single tuple/interval from tuples_list
#Output: the interval size of that tuple/interval
def interval_size(tup):
    return tup[1]-tup[0]

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    tuples_list.sort(key = interval_size)
    for i in range(len(tuples_list)-1):
        if interval_size(tuples_list[i]) == interval_size(tuples_list[i+1]):
            if tuples_list[i][0] > tuples_list[i+1][0]:
                tuples_list[i], tuples_list[i+1] = tuples_list[i+1], tuples_list[i] 
                
    return tuples_list

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

  return "all test cases passed"

def main():
  # open file intervals.in and read the data and create a list of tuples
    numintervals = int(sys.stdin.readline().strip())
    tuples_list = []
    for i in range(numintervals):
        num = (sys.stdin.readline().strip())
        nums = num.split()
        tuples_list.append((int(nums[0]), int(nums[1])))
    
    # merge the list of tuples
    tuples_list = merge_tuples(tuples_list)
    print(tuples_list)
    
  # sort the list of tuples according to the size of the interval
    tuples_list_sorted = sort_by_interval_size(tuples_list)

  # write the output list of tuples from the two functions
    
    print(tuples_list_sorted)

if __name__ == "__main__":
  main()