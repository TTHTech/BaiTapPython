# 6.9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one
# method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or
# 'campers' (Octothorpe). Create one object from each and print what it eats.
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print("Bear eats:", bear.eats())
print("Rabbit eats:", rabbit.eats())
print("Octothorpe eats:", octothorpe.eats())
