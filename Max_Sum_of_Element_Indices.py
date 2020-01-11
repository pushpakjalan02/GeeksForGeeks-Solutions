# Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed
# https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/

import sys

def find_max(list_of_nos):
    sum_element_index = 0
    sum_element_only = 0
    for i in range(1, len(list_of_nos)):
        sum_element_only += list_of_nos[i]
        sum_element_index += i * list_of_nos[i]

    max_value = sum_element_index
    for i in range(1, len(list_of_nos)):
        sum_element_index = sum_element_index - sum_element_only + (len(list_of_nos) - 1) * list_of_nos[i-1]
        if(sum_element_index > max_value):
            max_value = sum_element_index
        sum_element_only = sum_element_only - list_of_nos[i] + list_of_nos[i - 1]

    return max_value

def main():
    nos = int(input("Enter No. of Nos. "))
    list_of_nos = list(map(int, input("Enter the Nos.: ").strip().split()))
    if(len(list_of_nos) != nos):
        print("Invalid Input")
        sys.exit()
    max_value = find_max(list_of_nos)
    print("Maximum value is: ", max_value)
    return

if __name__ == "__main__":
    main()
