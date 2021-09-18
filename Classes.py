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

#price increased in a year for honda
print(honda.price)
honda.price_inc()
print(honda.price)

#price increased in a year for tata
print(tata.price)
tata.price_inc()
print(tata.price)