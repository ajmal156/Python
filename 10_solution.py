char_type =(input("ENTER THE  DOG TYPE:"))
char_age =int (input("ENTER THE DOG AGE:"))

if char_type=="pupi":
    if char_age<=3:
        print("pupy food")
    else:
        print("Adult food")

elif char_type=="dog":
    if char_age>6:
        print("Senior food dog")
    else:
        print("Junior food dog")
else:
    print("Sorry, Invalid Syntax try again")                        

