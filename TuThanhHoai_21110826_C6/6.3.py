# 6.3. Make yet another class called, of course, Thing3. This time, assign the value
# 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to
# make an object from the class to do this?
class Thing3:
    def __init__(self):
        self.letters = 'xyz'

example = Thing3()

print(example.letters)
