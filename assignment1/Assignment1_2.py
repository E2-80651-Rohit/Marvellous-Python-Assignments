def ChkNum(value1):
    if (value1 % 2)== 0:
        print("Even number")
    else:
        print("odd number")


def main():
    print("Enter number to search")
    no1 = int(input())
    ChkNum(no1)

if __name__ == "__main__":
    main()


