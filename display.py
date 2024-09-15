# import math 
# from turtle import*

# def hearta(k):
#     return 15 * math.sin(k)**3

# def heartb(k):
#     return 12 *math.cos(k)-5*\
#     math.cos(2*k)-5*\
#     math.cos(3*k)-\
#     math.cos(4*k)

# speed(6000)
# bgcolor("White")

# for i in range(60000):
#     goto(hearta(i)*20 ,heartb(i)*20)
#     for g in range(5):
#         color("red")
#     goto(0,0)
# done()    

from getpass import getpass

username = input("Enter Username: ")
password = getpass("Enter Password: ")

print(f"Username entered: {username}")
print(f"Password entered: {'*' * len(password)}") 