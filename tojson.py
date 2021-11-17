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
        auto = {
            "name":self.name,
            "brand":self.brand,
            "price":self.price,
            "year":self.year
        }
        with open(''+self.name+'.json', 'w') as jsFile:
            jsFile.write(json.dumps(auto, indent=4))
        print(auto)



obj1 =Brand("toyota",5000)
obj = Product("auto","toyota",1000,2000)
obj.tojson()