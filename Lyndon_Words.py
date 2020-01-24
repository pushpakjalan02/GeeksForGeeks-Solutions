# Generating Lyndon words of length n

# URL: https://www.geeksforgeeks.org/generating-lyndon-words-of-length-n/

import sys

def sort(list_of_characters):
    for i in range(0, len(list_of_characters) - 1):
        for j in range(0, len(list_of_characters) - i - 1):
            if(list_of_characters[j] > list_of_characters[j+1]):
                temp = list_of_characters[j]
                list_of_characters[j] = list_of_characters[j+1]
                list_of_characters[j+1] = temp
    return

def find_lyndon(list_of_characters, length):
    
    return

def main():
    length = int(input("Enter Length"))
    list_of_characters = list(input("Enter List of Characters").strip().split())
    if(len(list_of_characters) < length):
        sys.exit()
    sort(list_of_characters)
    find_lyndon(list_of_characters, length)
    return

if __name__ == "__main__":
    main()
