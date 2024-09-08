class Car:
    def __init__(self ,brand ,model):
        self.brand = brand
        self.model = model

    def Full_stack(self):
        return f"{self.brand} {self.model}"



new_car = Car("Toyota" ,"Alto")

print(new_car.brand)
print(new_car.model)
print(new_car.Full_stack())