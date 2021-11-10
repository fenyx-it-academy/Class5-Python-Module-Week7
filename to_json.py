import json
class Product:

    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    def toJson(self):
        return json.dumps(self,default=lambda o:o.__dict__,sort_keys=True,indent=4)


class Brand:

    def __init__(self,name,year):
        self.name = name
        self.year = year

roche_ferrero = Brand('roche_ferrero',1960)
chocolate = Product('chocolate',roche_ferrero,15 )

print(chocolate.toJson())
