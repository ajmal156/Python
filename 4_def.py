import math 

def cirul_squ(radius):
    area =2* math.pi * radius **2
    ciculference=math.pi*radius**2
    return area ,ciculference
a ,c =(cirul_squ(3))

print(f"Area: {a:.2f}")
print(f"Circulference: {c:.3f}")