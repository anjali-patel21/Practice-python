# You are given two values a and b. 
# Perform integer division and print a/b.


N = int(input())
a=[]
for i in range(N):
    a.append(input().split())

for i in range(len(a)):
    try:
        print(int(a[i][0])//int(a[i][1]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as v:
        print("Error Code:",v)
    
