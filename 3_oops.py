class Person():
    def __init__(self ,name ,age):
        self._name =name
        self._age =age

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    def com(self):
        return f"Name :{self._name} , Age :{self._age}"
p = Person("Farada" ,23)

print(p.get_name())
print(p.get_age())
print(p.com())
