'''
 4.define a class named american which has a static method called print nationality
 hint:use @staticmethod decorator to define class static method
'''
class American:
    name="America"
    @staticmethod
    def country(c):
        print(f"iam from {c}")

    def printnationality(self):
        self.country(self.name)

A=American()
A.printnationality()
American.country("america")
