def add_factorial(value):
    add = 0
    for i in range(1,value):
        if (value % i == 0):
            add = add + i

    return add
    

def main():
    print("Enter the number")
    no = int(input())

    ret = add_factorial(no)
    print("addition of Factorials of given number is:",ret)

if __name__ == "__main__":
    main()