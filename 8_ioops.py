number =int (input("Enter the number:"))
prime_num =True

if number>1:
        for num in range(2 ,number):
         if number% num == 0:
              prime_num=False

print("Prime number is:" ,prime_num)            