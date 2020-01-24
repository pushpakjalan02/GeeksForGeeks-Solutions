# Turn an image by 90 degree

# URL: https://www.geeksforgeeks.org/turn-an-image-by-90-degree/

import sys

def rotate(src_matrix, rows, columns):
    dest_matrix = [[0 for i in range(0, rows)] for j in range(0, columns)]
    for i in range(0, rows):
        for j in range(0, columns):
            dest_matrix[j][rows - i - 1] = src_matrix[i][j] 
    return dest_matrix

def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end = " ")
        print()

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
    print_matrix(dest_matrix)
    return

if __name__ == "__main__":
    main()
