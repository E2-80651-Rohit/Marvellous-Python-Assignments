def checkMinimum(List1):
    min_val = List1[0]

    for i in List1:
         if i <min_val:
             min_val = i
    return min_val


def main():
    print("Enter number of elements")
    size = int(input())

    Data = []
    print("Enter the numbers")
    for i in range(size):
        i = int(input())
        Data.append(i)
    
    ret = checkMinimum(Data)

    print("Minimum number in the list is",ret)



if __name__ == "__main__":
    main()