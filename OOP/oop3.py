#inheritance
# users 
#     - Wizard
#     - Archer


# Inheritance  
class User():
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self,name, power, email):
        super().__init__(email) # super
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


#introspection

wizard1 = Wizard('Merlin', 20,'merlin@gmail.com')
archer1 = Archer('Robin',50)

print(dir(wizard1))
# wizard1.attack()
# archer1.attack()

#print(isinstance(wizard1,User))
# polimorphism
def playerAttack(char):
    char.attack()

playerAttack(wizard1)
