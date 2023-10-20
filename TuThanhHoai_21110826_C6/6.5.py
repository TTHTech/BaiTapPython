# 6.5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol':
# 'H', 'number': 1. Then, create an object called hydrogen from class Element using
# this dictionary.
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

element_data = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**element_data)

print("Name:", hydrogen.name)
print("Symbol:", hydrogen.symbol)
print("Number:", hydrogen.number)
