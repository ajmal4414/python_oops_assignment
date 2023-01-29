'''
6.define a class named circle which can be constructed by a radius.the circle
class has a method which can compute the area
hint: use def method name(self)to define a method
'''
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(self.radius**2*3.14)
A=Circle(3)
A.area()