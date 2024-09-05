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


# def actual(operations):
#     def perform_operations(*args):
#         if len(args) < 2:
#             return "Error: At least two values required"

#         result = args[0]
#         for i in range(1, len(args)):
#             y = args[i]
#             for operation in operations:
#                 if operation == "add":
#                     result += y
#                 elif operation == "subtract":
#                     result -= y
#                 elif operation == "multiply":
#                     result *= y
#                 elif operation == "divide":
#                     if y != 0:
#                         result /= y
#                     else:
#                         return "Error: Division by zero"
#                 elif operation == "power":
#                     result **= y
#                 else:
#                     return "Error: Unknown operation"
#         return result
#     return perform_operations

# # Creating functions for various complex operations
# add_multiply = actual(["add", "multiply"])
# subtract_divide = actual(["subtract", "divide"])
# power_multiply = actual(["power", "multiply"])

# # Testing with multiple inputs
# print(add_multiply(2, 3, 4))               # (2 + 3) * 4 = 20
# print(subtract_divide(20, 5, 2))            # (20 - 5) / 2 = 7.5
# print(power_multiply(2, 3, 2))              # (2^3) * 2 = 16

# # More complex example with nested-like behavior
# combine_ops_complex = actual(["add", "multiply", "subtract"])
# print(combine_ops_complex(1, 2, 3, 4))     # ((1 + 2) * 3) - 4 = 5
