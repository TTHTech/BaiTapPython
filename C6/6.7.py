# 6.7. Call print(hydrogen). In the definition of Element, change the name of method
# dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f"Name: {self.name}\nSymbol: {self.symbol}\nNumber: {self.number}"

hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen)
