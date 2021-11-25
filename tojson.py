import json

class Brand():
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

class Product(Brand):
    def __init__(self,name,brand,price,year):
        super().__init__(brand,year)
        self.name = name
        self.brand = brand
        self.price = price
        # self.year = year
    

    def tojson(self):
        sneakers = {
            "name":self.name,
            "brand":self.brand,
            "price":self.price,
            "year":self.year
        }
        with open(''+self.name+'.json', 'w') as jsFile:
            jsFile.write(json.dumps(sneakers, indent=4))
        print(sneakers)



obj1 =Brand("nike",200)
obj = Product("sneakers","nike",200,2021)
obj.tojson()