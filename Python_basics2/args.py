# *args **kwargs

def superFunc(*args, **kwargs):
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(superFunc(1,2,3,4,5, num1=5,num2=10))


#Rule: params, *args, default pramenters, **kwargs