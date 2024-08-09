age =(int)(input("ENTER THE AGE:"))
day=input("ENTER THE DAY:")
if age >=101:
   print("This age is not define")
   exit()  
price =50 if age>25 else 40
if day=="Wnesday":
 price-=5

print("Ticket price for you in $",price)