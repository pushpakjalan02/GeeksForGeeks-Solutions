# Reversal algorithm for right rotation of an array
# Given an array, right rotate it by k elements.

# URL: https://www.geeksforgeeks.org/reversal-algorithm-right-rotation-array/

import sys

def reverse(list_of_nos, start, end):
    while(start < end):
        temp = list_of_nos[start]
        list_of_nos[start] = list_of_nos[end]
        list_of_nos[end] = temp
        start = start + 1
        end = end - 1
    return

def rotate(list_of_nos, nos, rotations):
    reverse(list_of_nos, 0, nos - 1)
    reverse(list_of_nos, 0, rotations - 1)
    reverse(list_of_nos, rotations, nos - 1)
    return

def main():
    nos = int(input("Enter No. of Nos.: "))
    list_of_nos = list(map(int, input("Enter List of Nos.: ").strip().split()))
    if(len(list_of_nos) != nos):
        sys.exit(0)
    rotations = int(input("Enter No. of Rotations.: "))
    rotate(list_of_nos, nos, rotations)
    print(list_of_nos)
    return

if __name__ == "__main__":
    main()
