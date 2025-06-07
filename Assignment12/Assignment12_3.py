class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value: "))
        self.Value2 = int(input("Enter second value: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2

def main():
    obj = Arithmetic()
    obj.Accept()
    print("Addition:", obj.Addition())
    print("Subtraction:", obj.Subtraction())
    print("Multiplication:", obj.Multiplication())
    print("Division:", obj.Division())

if __name__ == "__main__":
    main()
