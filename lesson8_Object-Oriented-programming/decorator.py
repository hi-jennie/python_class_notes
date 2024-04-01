
def len(func):
    names = []
    def inner(*args, **kwargs):
        name = func(*args, **kwargs)
        names.append(name)
        return name
    return inner

@len("/{a}*")
def get_name():
    name = input("What's your name?")
    return name

get_name()
print(get_name.__name__)

