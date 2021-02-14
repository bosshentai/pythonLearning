class PlayerCharacter:

    # Class Object Atribute 
    menbership = True

    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name #attribute
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        
    def run(self,hello):
        print(f'{self.name} is Running')

    @classmethod 
    def addingThings(cls,num1,num2):
        return cls('Teddy', num1 + num2)

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom',21)


player3 = PlayerCharacter.addingThings(2,3)

print(player3.age)

#print(player1.addingThings(2,3))
# print(player1.menbership)
# print(player1.shout())
# print(player1.run('hello'))
#player2.attack = 50 
# help(player1)
# print(player1.name)
# print(player2.age)
# print(player1.run())
# print(player2.attack)