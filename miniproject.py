item ={
    'coffee':90,
    'chai' :50,
    'pasta' :120,
    'roast' :250,
    'frice' :80,
    'pizza' :200,
    'sandwich': 150,
    'soup': 70,
    'salad': 100,
    'tea': 40,
    'ice cream': 60,
    'samosa': 30,

}

print("Welcome To my Python Restrouent.")
print("Menu")
print("Coffee :90\nchai :50\nPasta :120\nRoast :250\nFrice :80")
print("Pizza : 200\nSandwich : 150\nSoup : 70\nSalad : 100\nTea : 40")
print("Ice Cream : 60\nSamosa : 30")


order_total = 0
item_1 =input("Enter The Menu Item:").strip().lower()
if item_1 in item:
    order_total += item[item_1]
    print(f"The {item_1.capitalize()} has added to your order.")
else:
    print("Invalid order ,the order is not available.")

another_item =input("Would you like to add another item (Yes ,No):").lower()
if another_item == 'yes':
    item_2 =input("Enter the second order item :").strip().lower()
    if item_2 in item:
        order_total += item [item_2]
        print(f"The {item_2.capitalize()} has been added to your order.")
    else:
        print("Invalide order ,the order is not avalibal.")

print(f"The Total Amount for your  order Rs: {order_total}")        
