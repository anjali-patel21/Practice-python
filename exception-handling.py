# Exception handling in python

a = int(input("Enter value of number 1:"))
b = int(input("Enter value of number 2:"))

try:
    print("Execution started")
    print(a/b)

except ZeroDivisionError as e:                           # except block will only execute when error occurs
    print("You cannot divide any number by zero")

try:
    k = int(input("Enter value for k:"))
    print(k)

except ValueError as e:
    print("You need to enter integer value!!!")

finally:                                    # finally block will always execute
    print("Execution ended")
