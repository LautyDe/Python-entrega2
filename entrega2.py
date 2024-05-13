from classes.Person import Person

persona1 = Person('1', 'Lautaro', 25)


persona1.add_to_cart('Banana')
persona1.add_to_cart('Banana')
persona1.add_to_cart('Apple')
print(persona1)
print(len(persona1))
persona1.remove_from_cart('Banana')
print(persona1)
print(len(persona1))
persona1.buy()
print(persona1)