# Dictionary
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}


myList = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
},
{
    'a': [4,5,6],
    'b': 'hello',
    'x': True
}
]

print(myList[0]['a'][2])
print(dictionary['b'][1])


dictionary1 = {
    123: [1,2,3],
    True: 'Hello',
    'is_Magic': True
}

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.get('age',55))

print('basket' in user)
print('age' in user.keys())
print(user.items())