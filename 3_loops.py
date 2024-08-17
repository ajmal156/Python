number=int (input("ENTER THE TABLE:"))

for num in range(1 ,11):
    if num ==9:
        continue

    print(number ,'x',num ,'=' ,num*number)
