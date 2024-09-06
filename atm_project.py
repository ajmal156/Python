def check_pin():
   
    correct_pin ="1234"
    attempet= 3
    while attempet > 0:
        
        entere_pin =input("Enter the 4-Digit Code:")
       
        if entere_pin == correct_pin:
            print("PIN correct .Access granted!")
            return True
        else:
            attempet -=1
            print(f"Incorrect PIN. You have {attempet} attempts left.")

    print("To many incorrect attempts. Access denied!")
    return False

def showmenu():
    print("\n ATM Menu.")
    print("1. Current amount")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("1. Exit")

# check the money
def check_balance(balance):
    print(f"\nYour current balance is: {balance} Rs.")

# function for deposit money.
def deposit(balance):
    amount =float(input("Enter The Deposit Balance:"))
    if amount > 0:
        balance +=amount
        print(f"{balance} Rs is Deposit Succesfully")
    else:
        print("Sorry ,invalide amount.")
    return balance

# function for withdraw money.

def withdraw(balance):
    amount =float(input("Enter The Withdraw Balance:"))
    if 0 <amount <= balance:
        amount -=balance
        print(f"{amount} Rs is withdraw Succesfully.")
    else:
        print("Sorry ,Invalide amount!")
    return balance

def atm_system():
    balance =600
    
    if not check_pin():
        return
    while True:
        showmenu()
        choice =input("Choice in option(1,4):")

        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice =='3':
            balance = withdraw(balance)
        elif choice =='4':
            print("Thanks you for using atm ,GoodBy!")
            break
        else:
            print("Sorry ,Invalide choice please check again.")

atm_system()