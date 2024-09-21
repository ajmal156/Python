class Factorial():
    def __init__ (self ,number):
        self.number = number

    def Calculator(self):
        if self.number < 0:
            return "The factorial number not define by the negative number."
        if self.number == 0 or self.number == 1:
            return 1
        else:
            result =1
            for i in range(1 ,self.number +1):
                result *=i
            return result
        
number =int(input("Enter the number:"))
factorial =Factorial(number)

print(f"The factorial of {number} is {factorial.Calculator()}")

