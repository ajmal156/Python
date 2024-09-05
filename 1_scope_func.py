username ="Hello world"

def fun():
    username ="python"
    return username

print(username)
print(fun())

x =45

def fun2(y):
    number = x * y
    return number

result = fun2 (3)
print(result)

def fun3():
    global x
    x = 56

fun3()
print(x) 


def fun4():
    x = 45
    print("Inside function =" ,x)

fun4()
print("global function =" ,x)

def fun5():
    x = 89
    def fun6():
        print(x)
    return fun6
result =fun5()
result()

def actual(number):
    def num(y):
        return y ** number
    return num

f1 =actual(3)
f2 =actual(4)

print(f1(3))
print(f2(5))


# print(power_multiply(2, 3, 2))              # (2^3) * 2 = 16

# # More complex example with nested-like behavior
# combine_ops_complex = actual(["add", "multiply", "subtract"])
# print(combine_ops_complex(1, 2, 3, 4))     # ((1 + 2) * 3) - 4 = 5
