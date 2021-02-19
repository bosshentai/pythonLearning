from time import time 
def performance(fn):
    def wrapper(*args,**kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def longTime():
    print('1')
    for i in range(1000000000):
        i*5

@performance
def longTime2():
    print('2')
    for i in list(range(1000000000)):
        i*5
    

longTime()
longTime2()