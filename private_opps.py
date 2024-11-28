class Car:
    def __init__(self ,brand ,model ):
        self.__brand =brand
        self.model =model 

    def get_choice(self):
        return self.__brand +"!"
    
    def info(self):
        return f"Brand :{self.__brand} ,Model :{self.model}"
    

New_Car =Car("HONDA" ,"Civic")


print(New_Car.get_choice())
