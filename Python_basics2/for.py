# for item in 'Zero to mastery':
#     print(item)

# for item in [1,2,3,4,5]:
#     for x in ['a','b', 'c']:
#         print(item, x)

# iterable - list, dictionary, tuple, set , string 
# iterated -> one by one check each item in the collection. 

user = {
    'name': 'Golem',
    'age': 500,
    'canSwin' : False
}

# for item in user.items():
#     print(item)

for key , value in user.items():
    print(key, value)


# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)