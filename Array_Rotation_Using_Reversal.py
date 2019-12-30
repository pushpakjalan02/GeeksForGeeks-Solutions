import sys

def reverse(array, start, end):
    while(start < end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1
    return

def rotation(array, no, shift_no):
    reverse(array, 0, shift_no-1)
    reverse(array, shift_no, no-1)
    reverse(array, 0, no-1)

def main():
    no = int(input("Enter the No. of Nos.: "))
    array = list(map(int, input("Enter the Nos.: ").strip().split(maxsplit = no - 1)))
    if(len(array) != no):
        sys.exit()
    shift_no = int(input("Enter the Shift No.: "))
    rotation(array, no, shift_no)
    print(array)
    return
    
if __name__ == "__main__":
    main()
