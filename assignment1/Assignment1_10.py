def main():
    print("enter any name")
    name = input()

    print (len(name))
    ans = countChar(name)
    print(ans)

def countChar(na):
    count = 0
    for i in na:
        count = count + 1

    return count


if __name__ == "__main__":
    main()