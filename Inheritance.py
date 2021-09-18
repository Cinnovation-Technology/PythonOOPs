#A class can inherit attributes and behaviour methods from another class, called superclass
#A class which inherits from a superclass is called subclass, also called heir class or child class

#Code taken from Classes.py module

#Class made
class Car():
    #defined modelname yearm and price together
    def __init__(self,modelname,yearm,price):
        self.modelname = modelname
        self.yearm =  yearm
        self.price = price
#defined annual rise in the price

    def price_inc(self):
        self.price = int(self.price*1.15)

#values alloted to variables (variable = honda and tata)

honda = Car('HONDA CITY',2020,1000000)
tata = Car('TATA NEXON', 2021, 2200000)


#Superclass made named SuperCar
class SuperCar(Car):
    #defined the variables using init
    def __init__(self,modelname,yearm,price):
        super.__init__(modelname,yearm,price)


#values alloted to variables (variable = honda and tata)

honda = SuperCar('HONDA CITY',2020,1000000)
tata = Car('TATA NEXON', 2021, 2200000)

#print(help(honda))

honda.price_inc()
print(honda.price)