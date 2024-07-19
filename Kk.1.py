class Rectangle:
    def __init__(self,w,l):
       self.w=w
       self.l=l
    def area(self):
        return  self.w*self.l
    def perimeter (self):
       return 2*(self.w+self.l)
a=Rectangle(20,45)
print(f"area: {a.area()}")
print(f"perimeter: {a.perimeter()}")
