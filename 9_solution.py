year=int (input("ENTER THE YEAR:"))
if(year %400 ==0) or (year % 4==0 and year % 100 !=0):
    print(year,"is a reple year.")
else:
    print(year ,"is not a reple year.")    