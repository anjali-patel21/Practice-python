# Exception handling in python

a = int(input("Enter value of number 1:"))
b = int(input("Enter value of number 2:"))

try:
    print("Execution started")
    print(a/b)

except Exception:                           # except block will only execute when error occurs
    print("You cannot divide any number by zero")

finally:                                    # finally block will always execute
    print("Execution ended")
