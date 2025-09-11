class Emp:
    print("employee details")
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("slaray:",self.salary)
class Manager(Emp):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        print("Manager details:")
        super().display()
        print("department:",self.department)
a=Emp("yash",50000)
a.display()
b=Manager("yash",50000,"Finance")
b.display()