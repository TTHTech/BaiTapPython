# 6.4. Make a class called Element, with instance attributes name, symbol, and number.
# Create an object of this class with the values 'Hydrogen', 'H', and 1.
# Things to Do | 145

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
hydrogen = Element('Hydrogen', 'H', 1)

print("Name:", hydrogen.name)
print("Symbol:", hydrogen.symbol)
print("Number:", hydrogen.number)
