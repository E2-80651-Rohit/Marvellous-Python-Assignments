def check_prime(value):
    if value <=1:
        return False
    for i in range(2,value):
        if (value % i == 0):
            return False
        
    return True
    
    

def main():
    print("Enter the number")
    no = int(input())
    
    if check_prime(no):
        print(f"{no} is a prime number")
    else:
        print(f"{no} is not a prime number")

if __name__ == "__main__":
    main()