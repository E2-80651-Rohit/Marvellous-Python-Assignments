def checkMaximum(List1):
    max_val = List1[0]

    for i in List1:
         if i> max_val:
             max_val = i
    return max_val


def main():
    print("Enter number of elements")
    size = int(input())

    Data = []
    print("Enter the numbers")
    for i in range(size):
        i = int(input())
        Data.append(i)

    ret = checkMaximum(Data)

    print("Maximum number in the list is",ret)



if __name__ == "__main__":
    main()