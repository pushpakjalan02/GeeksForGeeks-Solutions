# Juggling Algorithm for Cyclic Shifting

import sys

def gcd(m, n):
    if(n == 0):
        return m
    else:
        return gcd(n, m%n)

def cyclically_shift(array, no, shift_no):
    gcd_no = gcd(no, shift_no)
    for i in range(0, gcd_no, 1):
        j = i
        temp = array[j]
        while(1):
            k = j + shift_no
            if(k >= no):
                k -= no
            if(i == k):
                break
            array[j] = array[k]
            j = k
        array[j] = temp
    return

def main():
    no = int(input("Enter no. of nos."))
    array = list(map(int,input("Enter Nos.").strip().split(maxsplit = no - 1)))
    if(len(array) != no):
        sys.exit()
    shift_no = int(input("Enter Shift No."))
    cyclically_shift(array, no, shift_no)
    print(array)
    return

if __name__ == "__main__":
    main()
