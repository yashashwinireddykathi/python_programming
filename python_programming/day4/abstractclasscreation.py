from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod        #abstract method
    def area(self):
        pass
class Rec(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of rectangle:",self.length*self.breadth)
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        a=2*3.14*self.r
        print(f"area of circle:{a:.2f}")
c=Circle(5)
c.area()
r=Rec(5,10)
r.area()
        
