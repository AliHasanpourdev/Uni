a=input().split()
a=[float(c)for c in a]
b=[]
for i in a:
    if i%1==0:
        b.append(int(i))
    else:
        b.append(i)
n=len(a)
for i in range (n):
    for j in range(0,n-i-1):
        if b[j]>b[j+1]:
            b[j],b[j+1] = b[j+1],b[j]
print(b)