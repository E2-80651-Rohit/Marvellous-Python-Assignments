def main():
    print("Enter a number to search")

    number =int(input())

    if (number > 0):
        print("Positive number")
    elif (number < 0):
        print("Negative number")
    else:
        print("Zero")

if __name__ == "__main__":
    main()