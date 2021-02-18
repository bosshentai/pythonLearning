#@classmethod
#@classstatic 

# Decorator


def myDecorator(func):
    def wrapFunc(gretting):
        print('************')
        func(gretting)
        print('***********')
    return wrapFunc 


@myDecorator
def hello(gretting):
    print(gretting)

hello('hello')