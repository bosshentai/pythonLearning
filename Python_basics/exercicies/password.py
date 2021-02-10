# input username
# input password 
# print password is  {} long 

userName = input('Enter your name \n')
userPassword = input('Enter your password \n')
passLength = len(userPassword)
encript = '*' * passLength

print(f'{userName}, your password {encript} is {passLength} letters long')