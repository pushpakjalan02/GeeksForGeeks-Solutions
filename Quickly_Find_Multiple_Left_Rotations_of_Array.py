# Quickly find multiple left rotations of an array | Set 1
# Given an array of size n and multiple values around which we need to left rotate the array. How to quickly find multiple left rotations?

# URL: https://www.geeksforgeeks.org/quickly-find-multiple-left-rotations-of-an-array/

import sys

def display_rotations(list_of_nos, nos, rotations):
    rotations = rotations % nos
    for i in range(rotations, rotations + nos):
        print(list_of_nos[i%nos], end = " ")
    return

def main():
    nos = int(input("Enter No. of Nos.: "))
    list_of_nos = list(map(int, input("Enter the Nos.: ").strip().split()))
    if(len(list_of_nos) != nos):
        print("Invalid Input.")
        sys.exit(0)
    rotations = int(input("Enter No. of Rotations: "))
    display_rotations(list_of_nos, nos, rotations)
    return

if __name__ == "__main__":
    main()
