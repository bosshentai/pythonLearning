from random import randint
import sys

#answer = randint(int(sys.argv[1]),int(sys.argv[2]))

answer = randint(1,10)

def runGuess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius')
            return True
    else:
        print('hey bozo, i said 1~10')
        return False

if __name__ == '__main__':
    answer = randint(1,10)
    while True:
        try:
            guess = int(input('quess a number 1~10: '))
            if (runGuess(guess,answer)):
                break
        except ValueError:
            print('please enter a number')
            continue

