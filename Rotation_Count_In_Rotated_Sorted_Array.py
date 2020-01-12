# Find the Rotation Count in Rotated Sorted array
# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

import sys

def main():
    nos = int(input("Enter No. of Nos.: "))
    list_of_nos = list(map(int, input("Enter the list of Nos. ").strip().split()))
    if(len(list_of_nos) != nos):
              print("Invalid Input.")
              sys.exit(0)
    pivot = find_pivot(list_of_nos, nos)
    print("No. of Rotations: ", pivot)
    return

if __name__ == "__main__":
    main()
