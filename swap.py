# swapping two values using 3rd variable
a = 20
b = 10
temp = a
a = b
b = temp
print("a = ",a)
print("b = ",b)

print("-----------------------")

# swapping two values without using 3rd variable
a = 12
b = 10
a = a-b
b = a+b
a = b-a
print("a = ",a)
print("b = ",b)

print("-----------------------")

# values can also be swapped directly (can be only done in python)
a,b = b,a
print("a = ",a)
print("b = ",b)
