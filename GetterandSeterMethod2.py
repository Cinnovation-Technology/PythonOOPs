class Edureka():
    def __init__(self):
        self.course = "Machine Learning Course"
        self.__tech = "Python"

    def Course(self):
        return self.course+ " : " + self.__tech
    def set__tech(self,x):
        self.__tech = x

    def get__tech(self):
        return self.__tech

ob = Edureka()

ob.set__tech("Scikit Learn")
print(ob.Course())