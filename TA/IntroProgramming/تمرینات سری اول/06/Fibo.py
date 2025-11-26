z = int(input())
x = 1
y = 1
if z>=2:
    for i in range(2,z):
       x , y = y , x+y
    print(y)
else:
    print(1)