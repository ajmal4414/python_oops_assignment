'''
1.define a class which has at two methods
getstring to get a string
printstring to print string in uppercase
'''
class test:
    def __init__(self):
        self.str1=""

    def getstring(self):
        self.str1=input("enter a string:")

    def printstring(self):
        print(self.str1.upper())

a=test()
a.getstring()
a.printstring()
