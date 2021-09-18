class Edureka():
    def __init__(self):
        self.course = "Python Programming Course"
        self.__tech = "Python"

# 2 underscore makes the variable private

    def CourseName(self):
        return self.course + " " + self.__tech

    def get__tech(self):
        return self.__tech

    def set__tech(self,t):
        self.__tech == t


ob = Edureka()

ob.set__tech("Machine Learning")

ob.get__tech()
# to unlock the private variable , we use name mangling method
# first write down the object and continue with class name and then the variable
# Example - print(ob._Edureka__tech)

print(ob.course)
print(ob._Edureka__tech)
print(ob.CourseName())
