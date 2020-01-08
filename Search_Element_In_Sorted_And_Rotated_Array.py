# Question @ https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

import sys

def binary_search(list_of_nos, start, end, search_val):
    if(start <= end):
        mid = int(start + ((end - start)/2))
        if(search_val == list_of_nos[mid]):
            return mid
        elif(search_val > list_of_nos[mid]):
            return binary_search(list_of_nos, mid+1, end, search_val)
        else:
            return binary_search(list_of_nos, start, mid-1, search_val)
    else:
        return -1

def search(list_of_nos, start, end, pivot):
    search_val = int(input("Enter Search Value: "))
    if(list_of_nos[start] <= search_val):
        if(pivot == 0):
            return binary_search(list_of_nos, start, end, search_val)
        else:
            return binary_search(list_of_nos, start, pivot-1, search_val)
    else:
        return binary_search(list_of_nos, pivot, end, search_val)
        

def search_pivot(list_of_nos, start, end):
    if(end - start + 1 == 1):
        return start
    elif(end - start + 1 == 2):
        if(list_of_nos[start] < list_of_nos[end]):
            return start
        else:
            return end
    else:
        mid = int(start + ((end - start)/2))
        if(list_of_nos[mid] < list_of_nos[mid+1] and list_of_nos[mid] < list_of_nos[mid-1]):
            return mid
        else:
            if(list_of_nos[mid] < list_of_nos[start]):                                          # search left
                return search_pivot(list_of_nos, start, mid-1)
            elif(list_of_nos[mid] > list_of_nos[end]):                                          # search right
                return search_pivot(list_of_nos, mid+1, end)
            else:
                return 0

def main():
    nos = int(input("Enter No. of Nos.: "))
    list_of_nos = list(map(int, input("Enter Nos.: ").strip().split(maxsplit = nos - 1)))
    if(len(list_of_nos) != nos):
        print("Invalid Input\n\n")
        sys.exit()
    pivot = search_pivot(list_of_nos, 0, nos - 1)
    ret_val = search(list_of_nos, 0, nos - 1, pivot)
    if(ret_val != -1):
        print("Found at Index: ", ret_val)
    else:
        print("Not Found")
        
    return

if __name__ == "__main__":
    main()
