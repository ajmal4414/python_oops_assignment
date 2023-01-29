'''
3.define a class which have a class parameter and have a same instance parameter
hints: define a instance parameter need add it in __init__method
you can init a object with construct parameter or set the value later
'''
class person:
    name=""

    def __init__(self,name):
        print(name)

person('john')