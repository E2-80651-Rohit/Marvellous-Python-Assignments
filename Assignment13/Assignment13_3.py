class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        return sum(i for i in range(1, self.Value) if self.Value % i == 0)

def main():
    obj = Numbers(int(input("Enter number: ")))
    print("Is Prime?", obj.ChkPrime())
    print("Is Perfect?", obj.ChkPerfect())
    print("Factors:")
    obj.Factors()
    print("Sum of Factors:", obj.SumFactors())

if __name__ == "__main__":
    main()
