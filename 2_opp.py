class ElectricCar:
    def __init__(self,model ,brand ,battery_size):
        self.model =model
        self.brand =brand
        self.battery_size =battery_size

    def full_stake(self):
        return f"{self.model} {self.brand} {self.battery_size}"
    

new_car =ElectricCar("Tasla" ,"Model P" ,"75 WKh")

print(new_car.model)
print(new_car.brand)
print(new_car.battery_size)
print(new_car.full_stake())