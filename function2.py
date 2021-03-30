# using keyword variable length argument

def person(name, *data):
    print(name)
    print(data)

person('Anjali', 20, 'surat', 7016832291)         # output: Anjali
                                                  #         (20,'surat',7016832291) ----> printed as a tuple

print('----------------------------------')

def personInfo(name, **data):
    print(name)
    print(data)

personInfo('Anjali', age = 20, city = 'surat', phno = 7016832291)       # age, city and phno are keywords
