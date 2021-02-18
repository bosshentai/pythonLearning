from time import time

def performance(fn):
    def wrapper(*args,**kawrgs):
        t1 = time()
        result = fn(*args,**kawrgs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper

@performance 
def longTime():
    for i in range(100000000):
        i*5

longTime()