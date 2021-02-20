# library  read about it 
# pathlib



# myFile = open('test.txt')

# # print(myFile.read())
# # myFile.seek(0)
# # print(myFile.read())
# # print(myFile.read())

# #print(myFile.readline())

# print(myFile.readlines())


# myFile.close()

# # read file 
try:
    with open('./data/test.txt',mode='r') as myFile:
        print(myFile.readlines())
except FileNotFoundError as err : 
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err


# #read and write file 
# with open('test.txt', mode='r+') as myFile:
#     text = myFile.write('hey it\' me')
#     print(text)


# # write file  with append 
# with open('test.txt', mode='a') as myFile:
#     text = myFile.write(':d')
#     print(text)


# write file  with write 
# can create a new file and over write 
# with open('sad.txt', mode='w') as myFile:
#     text = myFile.write(':(')
#     print(text)
