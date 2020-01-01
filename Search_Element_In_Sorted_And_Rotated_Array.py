# Question @ https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

import sys

def binary_search():

def search_pivot(list_of_nos, start, end, nos):
    if()
    mid = start + ((end - start)/2)
    if(list_of_nos[mid] > list_of_nos[mid+1] && list_of_nos[mid] > list_of_nos[mid-1]):
        return mid
    else:
        pivot = 
        return pivot

def main():
    nos = int(input("Enter No. of Nos.: "))
    list_of_nos = list(map(int, input("Enter Nos.: ").strip().split(maxsplit = nos - 1)))
    if(len(list_of_nos) != nos):
        print("Invalid Input\n\n")
        sys.exit()
    search_pivot(list_of_nos, 0, nos - 1)
    return

if __name__ == "__main__":
    main()
