# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:47:52 2021

@author: guobr
"""
import sys
#  File: Spiral.py

#  Description: Create a spiral given arbitrary dimensions.
#  returns sum of numbers adjacent to provided number

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 2/1/2021

#  Date Last Modified: 2/1/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral ( n ):
    if n % 2 == 0:
        n += 1
    dlist = [[0 for i in range(n)] for j in range(n)]
    mx = int(n/2 - 0.5)

    my = mx

    currCircle = 0
    RDLU = giveRDLU(currCircle)

    for curr in range(1,n*n+1):

        dlist[my][mx] = curr
        if RDLU[0] > 0:
            mx += 1
            RDLU[0] -= 1

        elif RDLU[1] > 0:
            my += 1
            RDLU[1] -= 1

        elif RDLU[2] > 0:
            mx -= 1
            RDLU[2] -= 1

        elif RDLU[3] > 0:
            my -= 1
            RDLU[3] -= 1
        else:
            currCircle += 1
            RDLU = giveRDLU(currCircle)
            mx += 1
            RDLU[0] -= 1


    return dlist

#returns list of needed directional steps to create next level of spiral
def giveRDLU(currCircle):
    steps = 6 + currCircle * 8
    r = steps // 4
    d = r
    l = r + 1
    u = l
    return [r,d,l,u]

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    x, y = 0, 0
    ans = 0
    found = False
    for i in range(len(spiral)):
        for j in range(len(spiral)):
            if spiral[i][j] == n:
                y,x = i, j
                found = True

    if found == False:
        return 0

    if x == 0:
        if y == 0:
            ans += spiral[y+1][x+1] + spiral[y+1][x]+ spiral[y][x+1]

        
        elif y == len(spiral) - 1:
            ans += spiral[y-1][x+1] + spiral[y][x+1] + spiral[y-1][x]

        else:
            ans += spiral[y-1][x] + spiral[y-1][x+1] + spiral[y][x+1] \
                + spiral[y+1][x] + spiral[y+1][x+1]

    elif x == len(spiral) - 1:
        if y == 0:
            ans += spiral[y][x-1] + spiral[y+1][x] + spiral[y+1][x-1]

        elif y == len(spiral) - 1:
            ans += spiral[y-1][x-1] + spiral[y-1][x] + spiral[y][x-1]

        else:
            ans += spiral[y][x-1] + spiral[y-1][x] + spiral[y-1][x-1] \
                + spiral[y+1][x-1] + spiral[y+1][x]

    elif y == 0:
        ans += spiral[y][x-1] + spiral[y+1][x-1] + spiral[y+1][x] \
            + spiral[y+1][x+1] + spiral[y][x+1]

    
    elif y == len(spiral) - 1:
        ans += spiral[y-1][x] + spiral[y-1][x-1] + spiral[y-1][x+1] \
            + spiral[y][x-1] + spiral[y][x+1]

    else:
        ans += spiral[y+1][x] + spiral[y+1][x-1] + spiral[y+1][x+1]
        ans += spiral[y][x+1] + spiral[y][x-1] + spiral[y-1][x-1] 
        ans += spiral[y-1][x] + spiral[y-1][x+1]

        
    return ans
                
                

def main():
  # read the input file
  spiralsize = int(sys.stdin.readline().strip())
  
  # create the spiral
  spiral = create_spiral(spiralsize)
  
  keepgoing = True
  
  while keepgoing:
      nextline = sys.stdin.readline().strip()
      if nextline == '':
          break
      # add the adjacent numbers
      currAdjacentSum = sum_adjacent_numbers(spiral, int(nextline))
      
      # print the result
      print(currAdjacentSum)

  

if __name__ == "__main__":
   main()
 



        

