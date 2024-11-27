class Car :
    Total_car =0
    def __init__(self ,brand ,model):
        self.brand =brand 
        self.model = model 
        Car.Total_car+=1

    def get_choice (self):
       return f"Brand :{self.brand} ,Model :{self.model}"

    def for_choice(self):
        return "Petrol OR Desiel."

class Electric_car(Car):
    def __init__(self, brand ,model ,battery_size):
        super().__init__(brand ,model)
        self.battery_size =battery_size
    
    def get_choice (self):
       return f"Brand :{self.brand} ,Model :{self.model} ,Battery_size :{self.battery_size}"

    def for_choice(self):
        return "Electric Charge."


Tesla=Electric_car("Tesla" ,"Model S" ,"85kwh")

print(Tesla.get_choice())
print(Tesla.for_choice())

New_car = Car("Toyota" ,"Corola")

print(New_car.for_choice())
print(f"Total Car : {Car.Total_car}")