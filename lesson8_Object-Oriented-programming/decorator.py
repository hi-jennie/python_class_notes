def wrapper(func):
    def inner(*args,**kwargs):
        print(1)
        ret = func(*args,**kwargs)
        print(2)
        return ret
    return inner

def wrapper1(func):
    def inner(*args,**kwargs):
        print(3)
        ret = func(*args,**kwargs)
        print(4)
        return ret
    return inner


def foo():
    print(5)

foo = wrapper(foo)
foo = wrapper1(foo)
foo()
