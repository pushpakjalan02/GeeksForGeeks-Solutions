import sys

def cyclically_shift_by_one(list_of_nos, nos):
    temp = list_of_nos[ nos - 1 ]
    for i in range(nos - 2, -1 , -1):
        list_of_nos[i+1] = list_of_nos[i]
    list_of_nos[0] = temp
    return

def main():
    nos = int(input("Enter No. of Nos.: "))
    list_of_nos = list(map(int, input("Enter the Nos.: ").strip().split(maxsplit = nos - 1)))
    if(len(list_of_nos) != nos):
       print("Invalid Input.\n\n")
       sys.exit(0)
    cyclically_shift_by_one(list_of_nos, nos)
    print(list_of_nos)
    return

if __name__ == "__main__":
    main()
