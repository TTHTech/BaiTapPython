# 6.8. Modify Element to make the attributes name, symbol, and number private. Define
# a getter property for each to return its value.

class Element:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def number(self):
        return self._number

hydrogen = Element('Hydrogen', 'H', 1)

print("Name:", hydrogen.name)
print("Symbol:", hydrogen.symbol)
print("Number:", hydrogen.number)
