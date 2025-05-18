import MarvellousNum 

def ListPrime(List1):
    sum = 0
    for i in List1:
        if MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum 

def main():
    print("Enter number of elements")
    size = int(input())

    Data = []
    print("Enter the numbers")
    for i in range(size):
        i = int(input())
        Data.append(i)

    ret = ListPrime(Data)

    print("sum of prime numbers from given list is:",ret)

if __name__ == "__main__":
    main()