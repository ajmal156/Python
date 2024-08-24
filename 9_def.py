def sum_number(limit):
    for num in range(1 ,limit+1 ,2):
        yield num 

for i in sum_number(5):
    print(i)

def num_of(number):
    for i in range(1 ,number+1):
        yield i**2

for num in num_of(4):
    print(num) 


def bet(num ,limit ):
    for multiply in range(num ,limit+1, num  ):
        yield multiply

for num in bet(2, 12):
    print(num)        


def number(get):
    factrial =1
    for num in range(1 ,get +1):
        factrial*=num
        yield factrial

for i in number(5):
    print(i)        
     
 

