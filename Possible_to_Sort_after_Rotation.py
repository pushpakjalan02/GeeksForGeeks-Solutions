# Check if it is possible to sort the array after rotating it

# URL: https://www.geeksforgeeks.org/check-if-it-is-possible-to-sort-the-array-after-rotating-it/

def find_answer(list_of_nos, nos):
    i = 0
    while(i < nos - 1):
        if(list_of_nos[i] > list_of_nos[i+1]):
            break
        i += 1
    if(i == nos - 1):
        return "Already Sorted... Hence Possible"
    i += 1
    while(i < nos - 1):
        if(list_of_nos[i] > list_of_nos[i+1]):
            break
        i += 1
    if(i == nos - 1):
        if(list_of_nos[0] < list_of_nos[nos - 1]):
            return "Not Possible"
        else:
            return "Possible"
    else:
        return "Not Possible" 
    return

def main():
    nos = int(input("Enter No. of Nos."))
    list_of_nos = list(map(int, input("Enter the list of Nos.").strip().split()))
    if(len(list_of_nos) != nos):
        return
    answer = find_answer(list_of_nos, nos)
    print(answer)
    return

if __name__ == "__main__":
    main()
