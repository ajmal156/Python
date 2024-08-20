fruit =["apple" ,"fruit" ,"apple" ,"banana" ,"fruit" ,"banana" ,"mango" ,"watermalan"]
quantity_value=set()

for char in fruit:
    if char in quantity_value:
        print( "Duplicate:",char)
        break

    quantity_value.add(char)        