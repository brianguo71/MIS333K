# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:54:39 2021

@author: guobr
"""
#  File: Poly.py

#  Description: Create Polynomials using linkedlist and methods to print,
#  add, and multiply polynomials together

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/16/21

#  Date Last Modified: 4/16/21
    
import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    current = self.first
    previous = self.first
    insert = Link(coeff, exp)

    # if the linkedlist is empty, add the value as the first  
    if current == None:
          insert.next = current
          self.first = insert
          return
    # find where the link that exp is less than
    while current.exp >= exp:
          previous = current
          current = current.next
          if current == None:
              # if we get to the end of the list without finding a link that our exp is less than, add it to the end
              previous.next = insert
              return
    # if current the first link (exp is less than every one of linkedlist's exps), add it to the front
    if current == self.first:
        insert.next = current
        self.first = insert
        return
    # otherwise, add it between previous and current (where previous is the last value to have a smaller exp and current is the first to have a larger exp)
    previous.next = insert
    insert.next = current
          

          

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
      selfcurrent = self.first
      pcurrent = p.first
      addList = LinkedList()

      # if either linkedlist is empty, return the other
      if selfcurrent == None:
          return p
      if p.first == None:
          return self
      
      # while both linkedlist have links remaining,
      while selfcurrent != None and pcurrent != None:
          # if the exponents are the same, add the coefficients together
          if selfcurrent.exp == pcurrent.exp:
              newcoeff = selfcurrent.coeff + pcurrent.coeff
              if newcoeff != 0:
                  addList.insert_in_order(newcoeff, selfcurrent.exp)
              selfcurrent = selfcurrent.next
              pcurrent = pcurrent.next
          # otherwise, add the larger of the two
          elif selfcurrent.exp > pcurrent.exp:
              addList.insert_in_order(selfcurrent.coeff, selfcurrent.exp)
              selfcurrent = selfcurrent.next
          else:
              addList.insert_in_order(pcurrent.coeff, pcurrent.exp)
              pcurrent = pcurrent.next
      # add remaining values from p
      while pcurrent != None:
        add = pcurrent.coeff
        # add all same exp elements together
        while pcurrent.next != None and pcurrent.exp == pcurrent.next.exp:
             add += pcurrent.next.coeff
             pcurrent = pcurrent.next
              
        addList.insert_in_order(add, pcurrent.exp)
        pcurrent = pcurrent.next
        
      # add remaining values from self  
      while selfcurrent != None:
          add = selfcurrent.coeff
          # add all same exp elements together
          while selfcurrent.next != None and selfcurrent.exp == selfcurrent.next.exp:
              add += selfcurrent.next.coeff
              selfcurrent = selfcurrent.next
              
          addList.insert_in_order(add, selfcurrent.exp)
          selfcurrent = selfcurrent.next
          
      return addList

  # helper method to simplify polynomials by adding same exponent elements together
  def simplify(self):
    # create a new linkedlist to be returned in the end
    newpoly = LinkedList()
    current = self.first
    if current == None:
        return None
    else:
        # add our first value into the list
        newpoly.insert_in_order(current.coeff, current.exp)
    while current.next != None:
        current = current.next
        # create a new linkedlist with the next link of self
        newlist = LinkedList()
        newlist.insert_in_order(current.coeff, current.exp)
        # use our add method we created to combine any possible same exponent elements
        newpoly = newpoly.add(newlist)
    return newpoly

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
      # if either one of the linkedlist is empty, return the other one
      if self.first == None:
          return p
      if p.first == None:
          return self
      
      selfcurrent = self.first
      multList = LinkedList()
      # for every value in our first linkedlist/ polynomial,
      while selfcurrent != None:
          pcurrent = p.first
          # we multiply them by every value in our second linkedlist/ polynomial
          while pcurrent != None:
              temppoly = LinkedList()
              temppoly.insert_in_order(pcurrent.coeff * selfcurrent.coeff, pcurrent.exp + selfcurrent.exp)
              # use add function to simplify any possible same-exponent elements
              multList = multList.add(temppoly)
              pcurrent = pcurrent.next

          selfcurrent = selfcurrent.next
                            
              
      return multList

  # create a string representation of the polynomial
  def __str__ (self):
      current = self.first
      ans = ""
      # return "" if polynomial is empty
      if current == None:
          return ans
      # add every element in coeff, exp form
      while current.next != None:
          ans += "(" + str(current.coeff) + ', ' + str(current.exp) + ') + '
          current = current.next
      # add last value with an additional ')' at the end
      ans += "(" + str(current.coeff) + ', ' + str(current.exp) + ')'
      return ans

def main():
  # read data from file poly.in from stdin
  numelements1 = int(sys.stdin.readline())
  # create polynomial p
  polyp = LinkedList()
  for i in range(numelements1):
      element = sys.stdin.readline().split()
      polyp.insert_in_order(int(element[0]), int(element[1]))

  emptyspace = sys.stdin.readline()
  
  # create polynomial q
  polyq = LinkedList()
  numelements2 = int(sys.stdin.readline())
  for i in range(numelements2):
      element = sys.stdin.readline().split()
      polyq.insert_in_order(int(element[0]), int(element[1]))

  # use my simplify method to simplify both polynomials
  polyp = polyp.simplify()
  polyq = polyq.simplify()
  
  # get sum of p and q and print sum
  sumpq = polyp.add(polyq)
  print(sumpq)

  # get product of p and q and print product
  multpq = polyp.mult(polyq)
  print(multpq)

if __name__ == "__main__":
  main()