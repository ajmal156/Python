class Person():
    def __init__ (self ,name ,age):
        self.name =name
        self.age =age
    
    def name_info(self):
        return f"Name : {self.name} Age : {self.age}"
    
class Employee(Person):
    def __init__ (self ,name ,age ,employee_id ,position):
        super(). __init__ (name ,age)
        self.employee_id =employee_id
        self.position =position

    def info_employee(self):
        return f"Employee_id : {self.employee_id}, Position : {self.position}"
    
new_employee =Employee("Ajmal" ,17 ,"E5645" ,"Software Engineer")

print(new_employee.name_info())
print(new_employee.info_employee())

