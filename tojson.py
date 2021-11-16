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

nike = Brand("running", 2021)
shoes = Product("shoes", nike, "100")
print(shoes.toJson())

