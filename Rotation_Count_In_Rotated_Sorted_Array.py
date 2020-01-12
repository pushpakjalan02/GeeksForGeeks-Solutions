# Find the Rotation Count in Rotated Sorted array
# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

import sys

def find_pivot(list_of_nos, start, end):
    if(start == end):
        return start
    elif(start == end - 1):
        if(list_of_nos[start] > list_of_nos[end]):
            return end
        else:
            return start
    elif(start < end):
        mid = int(start + ((end - start)/2))
        if(list_of_nos[mid] < list_of_nos[mid-1] and list_of_nos[mid] < list_of_nos[mid+1]):
            return mid
        elif(list_of_nos[mid] < list_of_nos[start]):
            return find_pivot(list_of_nos, start, mid-1)
        elif(list_of_nos[mid] > list_of_nos[end]):
            return find_pivot(list_of_nos, mid+1, end)
        else:
            return start
    
def main():
    nos = int(input("Enter No. of Nos.: "))
    list_of_nos = list(map(int, input("Enter the list of Nos. ").strip().split()))
    if(len(list_of_nos) != nos):
              print("Invalid Input.")
              sys.exit(0)
    pivot = find_pivot(list_of_nos, 0, nos - 1)
    print("No. of Rotations: ", nos - pivot)
    return

if __name__ == "__main__":
    main()
