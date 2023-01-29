'''
8.define a class named shape and it,s subclass square.
the square class has an init function which takes a length as argument.
both classes have a area function which can print the area of the shape where shape,s area is 0 by default
hint:to override a method in super class we can define a method with the same name in the superclass
'''
class shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0
class square(shape):
    def __init__(self,l):
        shape.__init__(self)
        self.length=l

    def area(self):
        return self.length*self.length
sq1=square(3)
print(sq1.area())