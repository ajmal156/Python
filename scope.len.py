
def actual(operations):
    def perform_operations(*args):
        if len(args) < 2:
            return "Error: At least two values required"

        result = args[0]
        for i in range(1, len(args)):
            y = args[i]
            for operation in operations:
                if operation == "add":
                    result += y
                elif operation == "subtract":
                    result -= y
                elif operation == "multiply":
                    result *= y
                elif operation == "divide":
                    if y != 0:
                        result /= y
                    else:
                        return "Error: Division by zero"
                elif operation == "power":
                    result **= y
                else:
                    return "Error: Unknown operation"
        return result
    return perform_operations

# Creating functions for various complex operations
add_multiply = actual(["add", "multiply"])
subtract_divide = actual(["subtract", "divide"])
power_multiply = actual(["power", "multiply"])


print(add_multiply(2, 3, 4))            
print(subtract_divide(20, 5, 2))           
print(power_multiply(2, 3, 2))             


combine_ops_complex = actual(["add", "multiply", "subtract"])
print(combine_ops_complex(1, 2, 3, 4))   
