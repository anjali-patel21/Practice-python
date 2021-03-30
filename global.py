# understanding global and local variables

a = 10                         # global variable

def variables():
    a = 9                      # local variable
    print("in function a:", a)

variables()

print("outside function a:", a)

print("---------------------------------")

# if i want to use global value of 'a' inside function?
def variables2():
    global a
    a = 15
    print("a in 2nd function:", a)

variables2()
print("a outside function:", a)
