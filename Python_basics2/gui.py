# Exercise ! 
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


# if find 0 display ' '
# if find 1 display .
def showTree():
    for row in picture:
        for pixel in row:
            if (pixel == 1):
                print('*',end='')
            else:
                print(' ',end='')
        print('')


showTree()