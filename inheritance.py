# inheritence in python

class fruits:

    def color(self):
        print("method of class fruit")

    def taste(self):
        print("second method of class fruit")

class apple(fruits):                               # here, apple ----> child class & fruits ----> parent class

    def cost(self):
        print("method of class apple")

class grapes(fruits):                              # here, grapes ----> child class & fruits ----> parent class

    def cost(self):
        print("method of class grapes")

f1 = fruits()
a1 = apple()
g1 = grapes()

f1.color()
f1.taste()

a1.taste()
a1.color()
a1.cost()

g1.taste()
g1.cost()
g1.color()
