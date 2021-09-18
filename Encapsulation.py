class Edureka():
    def __init__(self):
        self.course = "Python Programming Course"
        self.__tech = "Python"

# 2 underscore makes the variable private

    def CourseName(self):
        return self.course + " " + self.__tech

ob = Edureka()

# to unlock the private variable , we use name mangling method
# first write down the object and continue with class name and then the variable
# Example - print(ob._Edureka__tech)

print(ob.course)
print(ob._Edureka__tech)
print(ob.CourseName())
