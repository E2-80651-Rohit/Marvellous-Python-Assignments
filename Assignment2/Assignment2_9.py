def countDigit(value):

    if (value == 0):
        return 1
    value = abs(value)
    count = 0
    while(value>0): 
        value = value // 10
        count = count + 1
    return count

def main():
    print("Enter the number")
    no = int(input())

    ret = countDigit(no)
    print("number of digits in given number are:",ret)

if __name__ == "__main__":
    main()