# formatted strings

name = 'Hernani'
age = 27

print('hi ' + name + '. You are ' + str(age) + ' year old')

# python 3
print(f'hi {name}. You are {age} year old')

# python 2
print('hi {new_name}. You are {age} year old'.format(new_name='sally',age=100))