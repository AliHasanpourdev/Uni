n = int(input())
s = 0
for i in range(1,n+1) :
    if i==5 :
        continue
    s+=1/(i-5)
print(s)