def add(value1,value2):
    return value1 + value2

def main():
    print("enter first number")
    no1 = int(input())
    print("enter second number")
    no2 = int(input())

    result= add(no1,no2)

    print ("adition is:",result)
    
if __name__ == "__main__":
    main()