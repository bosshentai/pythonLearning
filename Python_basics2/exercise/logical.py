isMagician = True 
isExpert = False

# check if magician and expert : 
# "you are a master magician"
# if isMagician == True and isExpert == True:
#     print('you are a master magician')
# # check if magician but not expert:
# # "at least you're getting there"
# if isMagician == True and isExpert == False :
#     print('at least you\'re getting there')
# # if you're not a magician: 
# # "you need magic powers"
# if isMagician == False :
#     print("you need magic powers")

if isMagician and isExpert:
    print('you are a master magician')
elif isMagician and not isExpert:
    print('at least you\'re getting there')
elif not isMagician:
    print("you need magic powers")