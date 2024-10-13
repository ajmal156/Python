contacts = {}

def display_menu():
    print("\n--- Contact Book Application ---")
    print("1. View All Contacts")
    print("2. Add New Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def View_contact():
    if not contacts:
        print("---Contact No found!---")
    else:
        print("\n---Contact List---")
        for name ,number in contacts.items():
            print(f"Name : {name} ,Number : {number}")


def add_contact():
    name =input("Enter the contact name add: ")
    number  =int(input("Enter the contact phone number: "))
    contacts[name] =number
    print(f"Contact {name} added successfully.")

def search_contact():
    name = input(("Enter the seacrh to contact name:"))
    if name in contacts:
        print(f"Found Contact : Name :{name} ,Contact Number: {contacts[name]} ")
    else:
        print(f"No coutact found with the name '{name}'")

def delete_contact():
    name =input("Enter the delete to contact name: ")
    if name in contacts:
        del contacts[name]
    else:
        print(f"No coutact found with the name '{name}'")

while True:
    display_menu()

    try:
        choice =int(input("Enter the choice :"))
    except ValueError:
        print("Invalid number, Please enter the correct number ")
        continue

    if choice == 1:
        View_contact()
    elif choice == 2:
        add_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4 :
        delete_contact()
    elif choice == 5:
        print(("Exiting the application! Goodbye!"))
        break
    else:
        print("Invalid choice , please try again.")
    