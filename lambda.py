# code to filter the values from given list and then changing those filtered values using anonymous function

nums = [5,6,2,9,8,7,10,12,5]

evens = list(filter(lambda n:n%2==0,nums))    
print("filtered values: ",evens)

changevalue = list(map(lambda n:n+1,evens))
print("changed values: ",changevalue)
