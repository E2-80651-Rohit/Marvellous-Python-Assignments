def checkFrequency(List1,value):
    count = 0
    for i in List1:
        if (i == value):
            count = count + 1
    return count

def main():
    print("Enter number of elements")
    size = int(input())

    Data = []
    print("Enter the numbers")
    for i in range(size):
        i = int(input())
        Data.append(i)

    print("Enter the element to search it's frequency")
    no = int(input())

    ret = checkFrequency(Data,no)

    print(f"frequency of {no} is",ret)



if __name__ == "__main__":
    main()