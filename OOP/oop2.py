class PlayerCharacter:
    def __init__(self,name,age): # Dunder method
        self.name = name  #public variable
        self.__age = age  # private variable 
    
    def run(self):
        print('run')
    
    def speak(self):
        print(f'my name is {self._name}, and I and {self.__age} year old')


player1 = PlayerCharacter('andrei', 100)

# Encapsulation
print(player1.speak())