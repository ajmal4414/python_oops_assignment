'''
7 define a class named rectangle which can be constructed by a length and width. the rectangle class
has a method which can compute the area
hint:use def method name(self)to define a method
'''
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def rectangle_area(self):
        return self.length*self.width
r1=rectangle(6,4)
print(r1.rectangle_area())
r1.rectangle_area()