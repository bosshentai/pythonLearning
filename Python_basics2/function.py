#parameters
# Default Parametes
def sayHello(name='Darth',emoji=':)'):
    print(f'Hello {name} {emoji}')


# positional arguments
sayHello('Hernani', ':P')

# keyword argument 
# bad pratice 
sayHello(emoji=':P', name="hernani")
sayHello(name="leroy", emoji=":D")
sayHello()