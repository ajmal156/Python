class Car:
    def __init__ (self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def car_info(self):
        return f"Car: {self._make}, Model: {self._model}, Year: {self._year} "

my_car = Car("Toyota", "Corolla", 2021)


print(my_car.get_make())   
print(my_car.get_model())  
print(my_car.get_make())    
print(my_car.car_info())    
