Distance =int (input("ENTER THE DISTANCE:"))

if Distance<10:
    going="Wake"
elif Distance<15:
    going="Bike"
else:
    going="Car"

print("This Recomend For AI Transport Is:" ,going)