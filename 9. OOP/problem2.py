class Employee:
    compony = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

e = Employee("Jay", 100000000, 384002)
print(e.name, e.salary, e.pincode)
