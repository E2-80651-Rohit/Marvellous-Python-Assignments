class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_teacher(self):
        self.display_person()
        print(f"Subject: {self.subject}, Salary: {self.salary}")

def main():
    teacher = Teacher("P N Raut", 40, "Mathematics", 60000)
    teacher.display_teacher()

if __name__ == "__main__":
    main()
