# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:04:59 2021

@author: guobr
"""
#  File: BST_Cipher.py

#  Description: Using a BST, create an encrpytion and decryption method

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/23

#  Date Last Modified: 4/23

import sys

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        # insert every character that is a space or character
        for char in encrypt_str:
            if ord(char) == 32 or (ord(char) >= 97 and ord(char) <= 122):
                self.insert(char)
            else:
                continue
        return

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        new = Node(ch)
        current = self.root
        # if bst is empty, add node at root
        if current == None:
            self.root = new
            return
        while (current != None):
            # do not add existing characters
            if ch == current.data:
                break
            # if the character is less
            elif ch < current.data:
                # if the left child is empty, then add our node to our BST there
                if (current.lchild == None):
                    current.lchild = new
                    break
                # otherwise iterate and continue searching for a spot
                current = current.lchild
            # if the character is greater
            elif ch > current.data:
                # if the right child is empty, add our node to our BST there
                if (current.rchild == None):
                    current.rchild = new
                    break
                # otherwise, iterate and continue searching for a spot
                current = current.rchild

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        current = self.root
        ans = ""
        if current == None:
            return ''
        else:
            # go through bst
            while ch != current.data:
                # add < if ch is less than current and must go left
                if ch < current.data:
                    ans += '<'
                    current = current.lchild
                # add > if ch is greater than current and must go right
                elif ch > current.data:
                    ans += '>'
                    current = current.rchild
                # return '' if character does not exist
                if current == None:
                    return ''
            # after going through BST, if current is still the root, return '*'
            if current == self.root:
                return '*'
            # otherwise, return ans
            else:
                return ans

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        current = self.root
        # if root is empty, return ""
        if current == None:
            return ""
        # for every char in st,
        for char in st:
            # if char == '*', that means the char is the root, so we return the root
            if char == "*":
                return current.data
            # go left corresponding to the <
            elif char == '<':
                current = current.lchild
            # go right corresponding to the >
            elif char == '>':
                current = current.rchild
            # if the input does not lead to a valid char, return ""
            if current == None:
                return ""
        # after going left and right according to st, return current.data
        return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        st = st.lower()
        ans = ''
        # for every character in st,
        for char in st:
            # if they are valid characters, search and add them with a '!' at the end
            if ord(char) == 32 or ( 96 < ord(char) < 123):
                path = self.search(char)
                if path:
                    ans += path + '!'
        return ans[:-1]


    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):

        if (self.root != None):
            ans = ''
            #find a char for every !
            for char in st.split("!"):
                # use and append our traverse method to our ans
                trav = self.traverse(char)
                ans += trav
            return ans
            
def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()