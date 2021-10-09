# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:58:13 2021

@author: guobr
"""

#  File: Work.py

#  Description: Calculate the minimum number of codes needed to be written using binary and linear search

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 3/4/21

#  Date Last Modified: 3/4/21

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    n = v
    p = 1
    while (v//k**p) > 0:
        n += v//k**p
        p += 1
    return n
             
# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    for i in range(1, n+1):
        if sum_series(i, k) >= n:
            return i

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n, k):
    low = 0
    high = n
    mid = (high + low) // 2
    while low != mid and mid != high:
        if sum_series(mid, k) < n:
            low = mid
            mid = (high + low) // 2

        elif sum_series(mid, k) > n:
            high = mid
            mid = (high + low) // 2

        else:
            return mid

    return (mid + 1)
        
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()