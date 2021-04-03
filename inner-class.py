# class inside class in python

class data:
    subject = 'maths'

    def __init__(self):
        self.student1 = 45
        self.student2 = 49
        self.student3 = 50
        self.sb = self.sub()

    def total(self):
        return self.student1 + self.student2 + self.student3

    def show(self):
        print(self.student1, self.student3)

    class sub:
        def __init__(self):
            self.maths = 45
            self.english = 40

        def show(self):
            print("marks in maths:",self.maths)
            print("marks in english:",self.english)

c1 = data()
c2 = data()
c2.student3 = 48


print(c1.student1, data.subject)
print(c2.student2, c2.subject)
print(c1.student3, c2.student3)
print("Total marks:",c1.total)
print("total:",c1.total())
c2.sb.show()



