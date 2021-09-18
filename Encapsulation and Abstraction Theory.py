# Encapsuation

# Binding the data and code together as a single unit
# Securing data by hiding the implementation details to user.

# Abstraction

# Hides the implementation details and only provides the functionality to the user
# You can achieve abstraction using abstract classes and interfaces
# Abstract Class cannot bee instantiated
# It can only be inherited

# Object class 1 <--- Inherit Abstract <--- Abstract Class ---> X Object of Abstract Class
# ^^^ Diagram ^^^

# Abstraction Code

# Code taken from Inheritance.py module

#Class made

# Abstractmethod example
#for abc import ABC, abstractmethod

class Car():

    #@abstractmethod
    def price_inc(self):
        pass
#values alloted to variables (variable = honda and tata)

honda = Car('HONDA CITY',2020,1000000)
tata = Car('TATA NEXON', 2021, 2200000)


#Superclass made named SuperCar
class SuperCar(Car):
    #defined the variables using init
    def __init__(self,modelname,yearm,price):
        super.__init__(modelname,yearm,price)

    def price_inc(self):
        self.price = int(self.price * 2)


#values alloted to variables (variable = honda and tata)

honda = SuperCar('HONDA CITY',2020,1000000)
tata = Car('TATA NEXON', 2021, 2200000)

#print(help(honda))

honda.price_inc()
print(honda.price)