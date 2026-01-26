class Employee:
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

emp1 = Employee("alexa",22,1000,1234)
emp2 = Employee("bostero",23,2000,2234)
emp3 = Employee("kaith",20,2006,1007)
emp4 = Employee("kentut",21,2321,2111)

print(emp1.__dict__)
print(emp2.__dict__)
print(emp3.__dict__)
print(emp4.__dict__)

        