class  Car():
    count =0
    def __init__ (self ,model ,brand):
        self.__model  =model
        self._brand =brand
        Car.count+=1


    def Carclass(self):
        return "Patrol and deasile."
    @staticmethod
    def general_discprition():
        return "Car are means of transport."
    @property
    def model (self):
        return self.__model
    
class ElectrictCar(Car):
    def __init__(self, model, brand ,battery_size):
        super().__init__(model, brand)
        self.battery_size =battery_size    

    def info(self):
        return f"Model :{self.__model}, Brand : {self._brand}, Battery_size : {self.battery_size}"
    
    def Carclass(self):
        return "Electrict size"
    
    
    
new_car = ElectrictCar("City" ,"s20" ,"60KWh")

other_car =Car("Toyota" ,"Corola")

other_car.__model="city"
# print(new_car.info())
# print(new_car.Carclass())
# print(Car.count)
print(other_car.model)