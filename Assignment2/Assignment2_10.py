def AddDigit(value):

    add = 0
    while(value!=0):
        add = add + value % 10 
        value= value//10
    return add

def main():
    print("Enter the number")
    no = int(input())

    ret = AddDigit(no)
    print("addition digits in given number are:",ret)

if __name__ == "__main__":
    main()