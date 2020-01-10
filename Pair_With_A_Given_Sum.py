# Given a sorted and rotated array, find if there is a pair with a given sum
# https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

import sys

def search(list_of_nos, i , j, search):
    
    while(i != j):
        if(list_of_nos[i] + list_of_nos[j] == search):
            return True
        elif(list_of_nos[i] + list_of_nos[j] < search):
            i = (i + 1) % len(list_of_nos)
        else:
            j = (j - 1) % len(list_of_nos)
            
    return False

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
    nos = int(input("Enter No. of Nos."))
    list_of_nos = list(map(int, input("Enter the Nos.: ").strip().split()))
    
    if(len(list_of_nos) != nos):
        print("Invalid Input")
        sys.exit()

    search_val = int(input("Enter Sum to be Searched"))
    
    pivot = search_pivot(list_of_nos, 0, nos - 1)

    ret_value = search(list_of_nos, pivot % nos, (pivot - 1) % nos, search_val)
    print(ret_value)
    
    return

if __name__ == "__main__":
    main()
