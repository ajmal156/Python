def sum(a,b):
    return a +b
def subtract(a,b):
    return a -b
def multiply(a,b):
    return a *b
def divide(a,b):
    if b == 0:
        return "Zero ! Zero are not Divided."
    return a / b

print("Welcome To My Simple Calculator.")

def display_menu():
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def calculator():
    while True:
        display_menu()
        
        choice =input("Choose The menu in (1,5):")

        if choice =='5':
            print("Exit The Calculator ,GoodBy!")
            break

        if choice in ['1','2','3','4']:
            try:
                num_1 =int(input("Enter The First Number:"))     
                num_2 =int(input("Enter The Second Number:")) 
            except ValueError:
                print("Invalide number ,please check the numeric number")

            if choice =='1':
                result =sum(num_1 ,num_2)     
            elif choice =='2':
                result =subtract(num_1 ,num_2)     
            elif choice =='3':
                result =multiply(num_1 ,num_2)     
            elif choice =='4':
                result =divide(num_1 ,num_2)

            print(f"The Result is: {result}")
        else:
            print("Invalide num ,please check the verify number.")     

if __name__ =="__main__":
    calculator()