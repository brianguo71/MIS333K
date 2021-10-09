# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:35:23 2021

@author: guobr
"""

#  File: ExpressionTree.py

#  Description: Creates an expression tree to evaluate a given expression
#  prints the expression's result, as well as the infix and postfix 
#  versions of the expression

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/19/21

#  Date Last Modified: 4/19/21

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = Node(None)
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        current = self.root
        expressions = Stack()
        charlist = expr.split()
        
        for char in charlist:
            
            # if char is ( make a lChild, push our current node then update our current
            # node to be the lChild
            if char == '(':
                current.lChild = Node(None)
                expressions.push(current)
                current = current.lChild
                
            # if char is an operator, set current.data to char,
            # make an rChild, push our current node then update our current
            elif char in operators:
                current.data = char
                current.rChild = Node(None)
                expressions.push(current)
                current = current.rChild
            
            # if char is ) and if the stack/expressions isnt empty,
            # then make the current node equal to the parent node we pop
            elif char == ')':
                if expressions.is_empty() == False:
                    current = expressions.pop()
            # otherwise, set current.data to char and
            # make the current node equal to the parent node we pop
            else:
                current.data = float(char)
                current = expressions.pop()
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # if aNode.data is an operator
        if aNode.data in operators:
            # return the evaluation using the number on the left (lChild),
            # the operator (aNode.data) and the number on the right (rChild)
            return (self.operate(self.evaluate(aNode.lChild), self.evaluate(aNode.rChild), aNode.data))
        return aNode.data
            
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        # call recursive helper method
        strlist =  self.pre_order_helper(aNode, [])
        string = ""
        for char in strlist:
            # if the character is an integer, print it as such (removes decimal)
            if self.is_integer(char):
                string += str(int(char)) + ' '
            else:
                string += str(char) + ' '
        return string

    # helper method for pre_order
    # creates a list recursively that contains pre_order characters
    def pre_order_helper(self, aNode, curr):
        if aNode != None:
            curr.append(aNode.data)
            self.pre_order_helper(aNode.lChild, curr)
            self.pre_order_helper(aNode.rChild, curr)
        return curr
    
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        # call recursive helper method
        strlist = self.post_order_helper(aNode, [])
        string = ""
        for char in strlist:
            # if the character is an integer, print it as such (removes decimal)
            if self.is_integer(char):
                string += str(int(char)) + ' '
            else:
                string += str(char) + ' '
        return string
    
    # helper method for post_order
    # creates a list recursively that contains post_order characters
    def post_order_helper(self, aNode, curr):
        if aNode != None:
            self.post_order_helper(aNode.lChild, curr)
            self.post_order_helper(aNode.rChild, curr)
            curr.append(aNode.data)
        return curr
    
    # helper method used to evaluate integers
    def is_integer(self, n):
        if isinstance(n, int):
            return True
        if isinstance(n, float):
            return n.is_integer()
        return False

    # helper function used to evaluate individual operations
    def operate(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '//':
            return operand1 // operand2
        elif operator == '%':
            return operand1 % operand2
        elif operator == '**':
            return operand1 ** operand2
        
# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()