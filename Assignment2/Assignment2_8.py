def Display(value):
    for i in range(1,value+1):
        for j in range(1,i+1):
            print(j,end = "\t")
        print()

def main():
    print("Enter the number")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()