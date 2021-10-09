# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 01:00:18 2021

@author: guobr
"""
#  File: Reducible.py

#  Description: Finds largest word that can be reduced into continously smaller words

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number:  52230

#  Date Created: 4/3/21

#  Date Last Modified: 4/4/21
    
import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % const
  stepSize = const - (hash_idx % const)
  return stepSize

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  hash1 = hash_word(s, len(hash_table))
  if hash_table[hash1] == "":
      hash_table[hash1] = s
      
  else:
    secondhash = step_size(s, 13)
    i = 1
    while (hash_table[(hash1 + secondhash * i) % len(hash_table)] != ""):
      i += 1
      
    hash_table[(hash1 + secondhash * i) % len(hash_table)] = s
    
# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  lenWord = len(hash_table)
  hashIndex = hash_word(s, lenWord)

  if (hash_table[hashIndex] == s):
    return True

  elif (hash_table[hashIndex] != ""):
    hash2 = step_size(s, 13)
    i = 1
    while (hash_table[(hashIndex + hash2 * i) % len(hash_table)] != ""):
      if (hash_table[(hashIndex + hash2 * i) % len(hash_table)] == s):
        return True
      i += 1
      
  else:
      return False
  
  return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    
    if find_word(s, hash_memo):
        return True

    if len(s) == 1:
        if  s == 'a' or s == 'i' or s == 'o':
          return True
        else:
            return False

    reducedtable = reduceonce(s, hash_table)

    for child in reducedtable:
            t = is_reducible(child, hash_table, hash_memo)
            if t:
                insert_word(s, hash_memo)

                return True
    return False


def reduceonce(s, hash_table):
    ans = []
    for i in range(len(s)):
        newword = s[:i] + s[i+1:]
        if find_word(newword, hash_table):
            ans.append(newword)
    return ans

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    max = 0
    maxWords = []
    for i in range(len(string_list)):
        word = string_list[i]
        curr = len(word)

        if curr == max:
            maxWords.append(word)

        elif curr < max:
            continue

        elif curr > max:
            for j in range(len(maxWords)):
                maxWords.pop(0)
            maxWords.append(word)
            max = curr
    return maxWords

def main():
  # create an empty word_list
  word_list = []
  
  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append(line)
    
  word_list.append('a')
  word_list.append('o')
  word_list.append('i')

  # find length of word_list
  l = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  N = l * 2
  while (is_prime(N) == False):
      N += 1

  # create an empty hash_list
  hash_list = []
  
  # populate the hash_list with N blank strings
  for i in range(N):
    hash_list.append("")
        
  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
      insert_word(word, hash_list)
        
  # create an empty hash_memo of size M
  hash_memo = []
  
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  M = int(0.2 * l) + 1
  while is_prime(M) == False:
        M += 1
        
  # populate the hash_memo with M blank strings
  
  for i in range(M):
        hash_memo.append("")
  
  # create an empty list reducible_words
  reducible_words = []
  
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
      red = is_reducible(word, hash_list, hash_memo)
      if red:
          reducible_words.append(word)

  # find the largest reducible words in reducible_words
  maxReducWords = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  maxReducWords.sort()
  sort = sorted(maxReducWords)
  for word in sort:
      print(word)


if __name__ == "__main__":
  main()

