class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Name of the student",self.name)
        print("Roll no of the student",self.roll_no)
        print("Marks of the student",self.marks)
name=input("enter the name")
roll_no=int(input("enter the rollno"))
marks=int(input("enter the marks"))
c=Student(name,roll_no,marks)
c.display()
sname=input("enter the name")
sroll_no=int(input("enter the rollno"))
smarks=int(input("enter the marks"))
c1=Student(sname,sroll_no,smarks)
c1.display()