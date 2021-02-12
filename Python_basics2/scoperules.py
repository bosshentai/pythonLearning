# Scope rules

a = 1 

def confusion():
    a = 5
    return a 


print(a)
print(confusion()) 


#1 - start with local
#2 - Parent local ?
#3 - Global 
#4 - built in python functions.

c = 10
def confusion1(b):
    print(b)
    c= 90

confusion1(3000)


total = 0 
def count(total):
    total += 1
    return total


print(count(count(count(total))))