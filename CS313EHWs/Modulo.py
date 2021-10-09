#  File: Modulo.py

#  Description: Determines if a list of integers is closed under modulo (x % y is also a member # of the list for any nonzero x and y in the list)

#  Student Name: Brian Guo

#  Student UT EID: bg27773

#  Course Name: CS 313E

#  Unique Number: 52230

import sys

# Input: lst is a list of positive integers that includes 0
# Output: return True if for any 2 nonzero elements x and y in the list, x % y is also in the list
# return False otherwise

def is_closed_modulo(lst):
    for i in range(len(lst)):
        if lst[i] != 0:
            for k in range(len(lst)):
                if lst[k] != 0:
                    m = lst[i] % lst[k]
                    found = False
                    for j in range(len(lst)):
                        if m == lst[j]:
                            found = True
                    if found == False:
                        return False                     
    return True


def main(): 
    # read input file
    lst = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    # get result from your call to is_closed_modulo()
    result = is_closed_modulo(lst)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()