def specialFor(iterable):
    iterador = iter(iterable)
    while True:
        try:
            print(iterador)
            next(iterador)
        except StopIteration:
            break

specialFor([1,2,3])