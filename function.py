# defining a function
def update(x):
    x = 21
    print(x)

a = 10
update(a)

# using variable length argument
def add(a,*b):
    c = a
    for i in b:
        c = c + i
    print(c)

add(10,5,12,16)
add(15,5,10)
add(15,5,15,20,30)
