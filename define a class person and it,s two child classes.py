'''
 9.define a class person and it,s two child classes:Male and female. all classes have a method "get gender" which can
 print "male for male class and "Female" for female class"
# hint:use subclass(parentclass) to define a child class
'''
class person:
    def getGender(self):
        return "unknown"

class Male(person):
    def getGender(self):
        return "Male"

class Female(person):
    def getGender(self):
        return "Female"
male1=Male()
female1=Female()

print(male1.getGender())
print(female1.getGender())
