def factorial(value):
    fact = 1
    for i in range(1,value+1):
        fact = fact * i
    
    return fact
    

def main():
    print("Enter the number")
    no = int(input())

    ret = factorial(no)
    print("Factorial of given number is:",ret)

if __name__ == "__main__":
    main()