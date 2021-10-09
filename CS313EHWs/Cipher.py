# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:40:02 2021

@author: guobr
"""
import sys
#  File: Cipher.py

#  Description: Encrypt and decrypt strings by rotating them 90 degrees

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 2/8/2021

#  Date Last Modified: 2/8/2021

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
    ans = ''
    while len(strng) ** 0.5 % 1 != 0:
        strng += '*'
    for i in range(int(len(strng) - len(strng) ** 0.5), len(strng)):
        for j in range(i,-1, int(-(len(strng) ** 0.5))):
            if strng[j] != '*':
                ans += strng[j]
    return ans
    
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    ans = ''
    while len(strng) ** 0.5 % 1 != 0:
        strng += '*'
    anslist = ['*'] * len(strng)
    curindex = 0
    for i in range(int(len(strng) - len(strng) ** 0.5), len(strng)):
        for j in range(i,-1, int(-(len(strng) ** 0.5))):
            anslist[j] = strng[curindex]
            curindex += 1
    for i in anslist:
        if i != '*':
            ans += i
    return ans

def main():
  # read the two strings P and Q from standard imput
  P = sys.stdin.readline().strip()
  Q = sys.stdin.readline().strip()
  
  # encrypt the string P
  P = encrypt(P)
  # decrypt the string Q
  Q = decrypt(Q)
  
  # print the encrypted string of P and the 
  # decrypted string of Q to standard out
  print(P)
  print(Q)

if __name__ == "__main__":
  main()