# Find a rotation with maximum hamming distance
# Given an array of n elements, create a new array which is a rotation of given array and hamming distance between both the arrays is maximum.

# https://www.geeksforgeeks.org/find-a-rotation-with-maximum-hamming-distance/

import sys

def max_hamming_distance(list_of_nos, nos):
    
    return

def main():
    nos = int(input("Enter no. of nos.: "))
    list_of_nos = list(map(int, input("Enter List of Nos.").strip().split()))
    if(len(list_of_nos) != nos):
        sys.exit(0)
    max_hamming_distance(list_of_nos, nos)
    return

if __name__ == "__main__":
    main()
