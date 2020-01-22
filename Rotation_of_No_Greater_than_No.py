# Check whether all the rotations of a given number is greater than or equal to the given number or not

# URL: https://www.geeksforgeeks.org/check-whether-all-the-rotations-of-a-given-number-is-greater-than-or-equal-to-the-given-number-or-not/

def find_no_of_digits(no):
    i = 0
    while(no != 0):
        no = int(no / 10)
        i = i+1
    return i

def test_no(no, no_of_digits):
    temp = no
    for i in range(1, no_of_digits):
        temp = int(temp / 10) + (temp % 10) * int(pow(10, no_of_digits - 1))
        if(temp < no):
            return "False"
    return "True"

def main():
    no = int(input("Enter the No. "))
    no_of_digits = find_no_of_digits(no)
    print(test_no(no, no_of_digits))
    return

if __name__ == "__main__":
    main()
