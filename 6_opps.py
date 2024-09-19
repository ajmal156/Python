class engine():
    def engine_info(self):
        return "This is a engine"

class battery():
    def battery_info(self):
        return "This is a battery"
    
class Car:
    def __init__(self,brand ,model):
        self.brand =brand
        self.model =model
    
    def brand_car(self):
        return f" Brand: {self.brand}"

    def car_info(self):
        return f"Brand : {self.brand}  Model: {self.model}"
    
class Electrict_car(engine ,battery ,Car):
    def __init__(self, brand, model):
        Car.__init__(self ,brand, model)


new_tesla =Electrict_car("Tesla" ,"S20")

print(new_tesla.engine_info())
print(new_tesla.battery_info())
print(new_tesla.car_info())
print(new_tesla.brand)
    


