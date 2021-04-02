# using decorators

def div(a,b):
    print(a/b)

def modify_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = modify_div(div)

div(5,10)
