class Person:
    def __init__(self,Name ,Work):
        self.Name =Name
        self.Work =Work
    
    def info(self):
        return f"Name: {self.Name} ,Work: {self.Work}\nTHANKS"
    
    @staticmethod
    def disptrion():
        return "GENERAL DISPTRION !\nThere are the software enginer in 'Google Company'."

    @property
    def get_info(self):
        return  f"Work : '{self.Work}'!"

class information(Person):
    def __init__(self ,Name ,Work ,imploye_ID, Place):
        super().__init__(Name ,Work)
        self.imploye_ID =imploye_ID
        self.Place =Place

    def info (self):
        return f"Name: {self.Name} ,Work: {self.Work} ,Imploye_ID: {self.imploye_ID} ,Place: {self.Place}\nTHANKS"
    @property
    def get_info(self):
        return self.Name

class Proper_information(information):
    def __init__(self,Name ,Work ,Company ,imploye_ID ,Place ,Job_time ,Selary):
        super().__init__(Name ,Work ,imploye_ID ,Place)
        self.Job_time =Job_time
        self.Selary =Selary
        self.Company =Company

    def info(self):
        return f"Name: {self.Name}\nWork: {self.Work}\nCompany: {self.Company}\nImploye_ID: {self.imploye_ID}\nPlace: {self.Place}\nJob_time: {self.Job_time}\nSelary: {self.Selary}\nThanks"

    @property
    def get_info(self):
        return self.Place ,self.Job_time

new_imploye =information("Lad Mecola" ,"Software Enginer" ,"PA123456" ,"Europe")

print(new_imploye.info())

imploye =Person("Ajmal" ,"Software Enginer")

print(imploye.info())
print(imploye.get_info)

proper_imploye =Proper_information("Ajmal" ,"Software Enginer" ,"Microsoft" ,"PA567890" ,"Pakistan" ,"8AM To 4PM" ,"50 ,000")

print(proper_imploye.disptrion())  
 





