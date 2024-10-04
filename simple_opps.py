class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.color} {self.model} is now running.")
        else:
            print(f"The {self.model} is already running.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.model} has stopped.")
        else:
            print(f"The {self.model} is already stopped.")

# Creating an object of the Car class
my_car = Car("Toyota Corolla", "red")

# Using the methods
my_car.start()  # Start the car
my_car.start()  # Try starting the car again
my_car.stop()   # Stop the car
my_car.stop()   # Try stopping the car again
