# Find a rotation with maximum hamming distance
# Given an array of n elements, create a new array which is a rotation of given array and hamming distance between both the arrays is maximum.

# https://www.geeksforgeeks.org/find-a-rotation-with-maximum-hamming-distance/

import sys

def max_hamming_distance(list_of_nos, nos):
    max = -1
    sum = 0
    for i in range(0, nos):
        for j in range(0, nos):
            if(list_of_nos[j] != list_of_nos[(i + j) % nos]):
                sum += 1
        if(max < sum):
            max = sum
        sum = 0
    return max

def main():
    nos = int(input("Enter no. of nos.: "))
    list_of_nos = list(map(int, input("Enter List of Nos.").strip().split()))
    if(len(list_of_nos) != nos):
        sys.exit(0)
    max_val = max_hamming_distance(list_of_nos, nos)
    print("Maximum Hamming Distance: ", max_val)
    return

if __name__ == "__main__":
    main()
