#inheritance
# users 
#     - Wizard
#     - Archer


# Inheritance  
class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power {self.power}')

class Archer(User):
    def __init__(self,name,numArrows):
        self.name = name
        self.numArrows = numArrows

    def attack(self):
        print(f'attacking with arrows:arrows left- {self.numArrows}')

wizard1 = Wizard('Merlin', 20)
archer1 = Archer('Robin',50)
wizard1.attack()
archer1.attack()