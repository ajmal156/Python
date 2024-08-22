def print_statement(**kwargs):
    output =[]
    if 'fruit' in kwargs:
        print(f"Fruit: {kwargs['fruit'].upper()}")
        kwargs.pop('fruit')
    for key ,values in kwargs.items():
        output.append(f"{key.capitalize()}: {values}")
        print(" | ".join(output))

        print('-' * 20)

print_statement(fruit ="apple" ,qualitly ="fresh")
print_statement(fruit ="Sweets" ,qualitly ="fresh" ,price ="$12")
print_statement(fruit ="Pinaple" ,qualitly ="fresh" ,day="Wnesday" ,price ="$20")
print_statement(fruit ="Charry" ,qualitly ="Good" ,Expesive ="Charry")
print_statement(fruit ="Mango" ,qualitly ="fresh" ,price ="$15")
print_statement(fruit ="Watermalan" ,qualitly ="Yuesday")
print_statement(fruit ="apple" ,qualitly ="fresh")
print_statement(fruit ="banana" ,price ="$10") 
