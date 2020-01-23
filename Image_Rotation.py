# Turn an image by 90 degree

# URL: https://www.geeksforgeeks.org/turn-an-image-by-90-degree/

import sys

def rotate(matrix, rows, columns):
    dest_matrix = 
    for 
    return

def main():
    rows = int(input("Enter No. of Rows: "))
    columns = int(input("Enter No. of Columns: "))
    matrix = []

    print("Enter in matrix form")
    for i in range(0, rows):
        to_append = list(map(int, input().strip().split()))
        if(len(to_append) != columns):
            print("Invalid Input")
            sys.exit(0)
        matrix.append(to_append)
    dest_matrix = rotate(matrix, rows, columns)
    return

if __name__ == "__main__":
    main()
