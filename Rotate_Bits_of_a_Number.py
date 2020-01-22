# Rotate bits of a number

# URL: https://www.geeksforgeeks.org/rotate-bits-of-an-integer/

import sys

def main():
    no = int(input("Enter No."))
    rotate_by = int(input("Rotate by: "))
    print("After Left Rotate: ", ((no << rotate_by) + (no >> (32 - rotate_by))) & 0xffffffff)
    print("After Right Rotate: ", ((no << (32 - rotate_by)) + (no >> rotate_by)) & 0xffffffff)

    return

if __name__ == "__main__":
    main()
