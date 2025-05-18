def  addition(List1):
    addition = 0
    for i in List1:
        addition = addition  + i
    
    return addition

def main():
    print("Enter number of elements")
    size = int(input())

    Data = []
    print("Enter the numbers")
    for i in range(size):
        i = int(input())
        Data.append(i)

    ret = addition(Data)

    print("addition of numbers in list is",ret)



if __name__ == "__main__":
    main()