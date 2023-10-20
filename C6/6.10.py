# 6.10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method:
# does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (Smart
# Phone). Then, define the class Robot that has one instance (object) of each of these.
# Define a does() method for the Robot that prints what its component objects do

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        laser_action = self.laser.does()
        claw_action = self.claw.does()
        smartphone_action = self.smartphone.does()
        return f"Laser does: {laser_action}, Claw does: {claw_action}, SmartPhone does: {smartphone_action}"

robot = Robot()

print(robot.does())
