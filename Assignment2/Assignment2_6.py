def Display(value):
    for i in range(value,0,-1):
        for j in range(i):
            print("*",end = "\t")
        print()

def main():
    print("Enter the number")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()